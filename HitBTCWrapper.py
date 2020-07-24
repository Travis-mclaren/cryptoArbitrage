import HitBTC
from HitBTC import *
from decimal import *


class HitBTCWrapper:

	HitBTCApiKey = '<API KEY>'
	HitBTCApiSecret = '<API SECRET>'
	TradeFee = Decimal(0.001)
	tempCoins = {}
	allCoins = {}
	allCoinsBackwards = {}
	allMarkets = []


	def __init__(self):
		self.HitBTC = HitBTC( 'https://api.hitbtc.com', self.HitBTCApiKey, self.HitBTCApiSecret )


	def load_coin_names(self):
		res = self.HitBTC.get_currency()

		for coin in res:
			if coin['payinEnabled'] == True:
				self.tempCoins[coin['fullName'].upper()] = coin['id']

		return


	def filter_all_coins(self, matches):
		try:
			for key in self.tempCoins.keys():
				if key in matches:
					self.allCoins[key] = self.tempCoins[key]
					self.allCoinsBackwards[self.tempCoins[key]] = key
		except KeyError:
			pass

		return


	def load_all_markets(self):
		res = self.HitBTC.get_symbol_all()
		allMarkets = self.HitBTC.get_ticker_all()

		for market in res:
			try:
				if market['baseCurrency'].upper() in self.allCoinsBackwards.keys() and market['quoteCurrency'].upper() in self.allCoinsBackwards.keys():
					m = [m for m in allMarkets if m['symbol'] == market['id']][0]

					temp =	{
							 'Market': market['id']
							,'MarketCurrencyLong' : self.allCoinsBackwards[ market['baseCurrency'].upper() ]
							,'BaseCurrencyLong' : self.allCoinsBackwards[ market['quoteCurrency'].upper() ]
#							,'MinTradeSize' : None
							,'Last' : m['last']
							,'Bid' : m['bid']
							,'Ask' : m['ask']
							,'High' : m['high']
							,'Low' : m['low']
							,'BaseVolume' : m['volumeQuote']
							}

					self.allMarkets.append( temp )
			except KeyError:
				pass
		return


	def get_all_bids_over_threshold( self, symbol, price ):
		res = self.HitBTC.get_orderbook( symbol )
		quantity = 0

		for order in res['bid']:
			if Decimal( order['price'] ) <= price:
				quantity += Decimal( order['size'] )

		return quantity


	def get_all_asks_under_threshold( self, symbol, price, quantityCap ):
		res = self.HitBTC.get_orderbook( symbol )
		quantity = 0
		openSales = []

		for order in res['ask']:
			if Decimal(order['price']) <= price and quantity + Decimal(order['size']) <= quantityCap:
				quantity += Decimal(order['size'])
				openSales.append( order )

		return openSales


	def get_wallet_address( self, symbol ):
		res = self.HitBTC.get_address( symbol )

		try:
			if res['error']['code'] != 503:
				res = self.HitBTC.create_address( symbol )
		except KeyError:
			pass

		return res['address']

	def make_withdrawl( self, currency, amount, address, networkFee, paymentID ):
		res = self.HitBTC.withdraw( currency, amount, address, None, paymentID )

		return res