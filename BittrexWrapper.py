import Bittrex
from Bittrex import *
from decimal import *
from time import sleep


class BittrexWrapper:

	BittrexApiKey = '<API KEY>'
	BittrexApiSecret = '<API SECRET>'
	TradeFee = Decimal( 0.0025 )
	tempCoins = {}
	allCoins = {}
	allCoinsBackwards = {}
	CoinTxFee = {}
	allMarkets = []


	def __init__(self):
		self.Bittrex = Bittrex( self.BittrexApiKey, self.BittrexApiSecret, 2, using_requests, API_V2_0 )
		self.tempCoins.clear()
		self.allCoins.clear()
		self.allMarkets.clear()


	def load_coin_names(self):
		res = self.Bittrex.get_currencies()

		if res['success'] == True:
			for coin in res['result']:
				if coin['IsActive'] == True:
					self.tempCoins[coin['CurrencyLong'].upper()] = coin['Currency']
					self.CoinTxFee[coin['CurrencyLong'].upper()] = coin['TxFee']

		return


	def filter_all_coins(self, matches):
		for key in self.tempCoins.keys():
			if key in matches:
				self.allCoins[key] = self.tempCoins[key]
				self.allCoinsBackwards[self.tempCoins[key]] = key

		return


	def load_all_markets(self):
		res = self.Bittrex.get_market_summaries()

		if res['success'] == True:
			for coin in res['result']:

				market = coin['Market']
				marketSummary = coin['Summary']

				if market['MarketCurrencyLong'].upper() in self.allCoins.keys() and market['BaseCurrencyLong'].upper() in self.allCoins.keys() and market['IsActive'] == True:

					temp = {
							 'Market' : market['MarketName'].upper()
							,'MarketCurrencyLong' : market['MarketCurrencyLong'].upper()
							,'BaseCurrencyLong' : market['BaseCurrencyLong'].upper()
							,'MinTradeSize' : market['MinTradeSize']
							,'Last' : marketSummary['Last']
							,'Bid' : marketSummary['Bid']
							,'Ask' : marketSummary['Ask']
							,'High' : marketSummary['High']
							,'Low' : marketSummary['Low']
							,'BaseVolume' : marketSummary['BaseVolume']
						}

					self.allMarkets.append(temp)
		return


	def get_all_bids_over_threshold( self, symbol, price ):
		res = self.Bittrex.get_orderbook( symbol, SELL_ORDERBOOK )
		quantity = 0

		if res['success'] == True:
			for order in res['result']['buy']:
				if Decimal( order['Rate'] ) <= price:
					quantity += Decimal( order['Quantity'] )

		return quantity


	def get_all_asks_under_threshold( self, symbol, price, quantityCap ):
		res = self.Bittrex.get_orderbook( symbol, SELL_ORDERBOOK )
		quantity = 0
		openSales = []

		if res['success'] == True:
			for order in res['result']['sell']:
				if Decimal(order['Rate']) <= price and quantity + Decimal(order['Quantity']) <= quantityCap:
					quantity += Decimal(order['Quantity'])
					openSales.append( order )

		return openSales


	def get_wallet_address( self, symbol ):

		while True:
			res = self.Bittrex.get_deposit_address( symbol )
			if res['success'] == True:
				address = res['result']['Address']
				break
			sleep(0.25)

		return address