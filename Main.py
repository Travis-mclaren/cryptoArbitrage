import Bittrex, HitBTC, BittrexWrapper, HitBTCWrapper, HelperFunctions
from Bittrex import *
from HitBTC import *
from BittrexWrapper import *
from HitBTCWrapper import *
from HelperFunctions import *
from decimal import *

GAIN_PERCENTAGE_THRESHOLD = Decimal( 2.00 )
GAIN_DOLLAR_THRESHOLD = Decimal( 20.00 )

bw = BittrexWrapper()
bw.load_coin_names()

hw = HitBTCWrapper()
hw.load_coin_names()

bKeys = set( bw.tempCoins.keys() )
hKeys = set( hw.tempCoins.keys() )

matches = bKeys.intersection( hKeys )

bw.filter_all_coins( matches )
hw.filter_all_coins( matches )

bw.load_all_markets()
hw.load_all_markets()

for bMarket in bw.allMarkets:
	for hMarket in hw.allMarkets:
	
		if Decimal( bMarket['BaseVolume'] ) > 10 and Decimal( hMarket['BaseVolume'] ) > 10:	
			if bMarket['MarketCurrencyLong'] == hMarket['MarketCurrencyLong'] and bMarket['BaseCurrencyLong'] == hMarket['BaseCurrencyLong']:
			
				if ( ( ( Decimal(bMarket['Bid']) / Decimal(hMarket['Ask']) ) - 1 ) * 100 ) > GAIN_PERCENTAGE_THRESHOLD:
					print( 'HitBTC to Bittrex on Ask > Bid' )
					print( 'Market Currency: ', bMarket['MarketCurrencyLong'] )
					print( 'Base Currency: ', bMarket['BaseCurrencyLong'] )
					print( 'Bittrex Market: ', bMarket['Market'] )
					print( 'HitBTC Market: ', hMarket['Market'] )
					print( 'Bittrex Volume: ', bMarket['BaseVolume'] )
					print( 'HitBTC Volume: ', hMarket['BaseVolume'] )
					print( 'HitBTC Ask: ', hMarket['Ask'] )
					print( 'Bittrex Bid: ', bMarket['Bid'] )
					print( 'Percent gain: ',  ( ( Decimal(bMarket['Bid']) / Decimal(hMarket['Ask']) ) - 1 ) * 100 )
					print( '\n' )
					openSales = hw.get_all_asks_under_threshold( hMarket['Market'], Decimal(bMarket['Bid']) * ( 100 + GAIN_PERCENTAGE_THRESHOLD ), bw.get_all_bids_over_threshold( bMarket['Market'], Decimal(bMarket['Bid']) ) )
					
#					bWallet = bw.get_wallet_address( bw.allCoins[ bMarket['MarketCurrencyLong'] ] )
#					hWallet = hw.get_wallet_address( hw.allCoins[ hMarket['MarketCurrencyLong'] ] )
					
#					print( bWallet )
#					print( hWallet )
					
#					print( lowest_profitable_trade( bw.get_all_bids_over_threshold( bMarket['Market'], Decimal(bMarket['Bid']) ), hMarket['Ask'], 0.25, bMarket['Bid'], 0.1, bw.CoinTxFee[ bMarket['MarketCurrencyLong'] ] ) )
					
					
#				elif ( ( ( Decimal(bMarket['Last']) / Decimal(hMarket['Ask']) ) - 1 ) * 100 ) > GAIN_PERCENTAGE_THRESHOLD:
#					print( 'HitBTC to Bittrex on Ask > Last' )
#					print( 'Market Currency: ', bMarket['MarketCurrencyLong'] )
#					print( 'Base Currency: ', bMarket['BaseCurrencyLong'] )
#					print( 'Bittrex Market: ', bMarket['Market'] )
#					print( 'HitBTC Market: ', hMarket['Market'] )
#					print( 'Bittrex Volume: ', bMarket['BaseVolume'] )
#					print( 'HitBTC Volume: ', hMarket['BaseVolume'] )
#					print( 'HitBTC Ask: ', hMarket['Ask'] )
#					print( 'Bittrex Last: ', bMarket['Last'] )
#					print( 'Percent gain: ', ( ( Decimal(bMarket['Last']) / Decimal(hMarket['Ask']) ) - 1 ) * 100 )
#					print( '\n\n' )
#					hw.get_all_asks_under_threshold( hMarket['Market'], Decimal(bMarket['Last']) * ( 100 + GAIN_PERCENTAGE_THRESHOLD ), bw.get_all_bids_over_threshold( bMarket['Market'], Decimal(bMarket['Last']) ) )
					
				
				elif ( ( ( Decimal(hMarket['Bid']) / Decimal(bMarket['Ask']) ) - 1 ) * 100 ) > GAIN_PERCENTAGE_THRESHOLD:
					print( 'Bittrex to HitBTC on Ask > Bid' )
					print( 'Market Currency: ', bMarket['MarketCurrencyLong'] )
					print( 'Base Currency: ', bMarket['BaseCurrencyLong'] )
					print( 'Bittrex Market: ', bMarket['Market'] )
					print( 'HitBTC Market: ', hMarket['Market'] )
					print( 'Bittrex Volume: ', bMarket['BaseVolume'] )
					print( 'HitBTC Volume: ', hMarket['BaseVolume'] )
					print( 'Bittrex Ask: ', bMarket['Ask'] )
					print( 'HitBTC Bid: ', hMarket['Bid'] )
					print( 'Percent gain: ', ( ( Decimal(hMarket['Bid']) / Decimal(bMarket['Ask']) ) - 1 ) * 100 )
					print( '\n' )
					openSales = bw.get_all_asks_under_threshold( bMarket['Market'], Decimal(hMarket['Bid']) * ( 100 + GAIN_PERCENTAGE_THRESHOLD ), hw.get_all_bids_over_threshold( hMarket['Market'], Decimal(hMarket['Bid']) ) )
					
#					bWallet = bw.get_wallet_address( bw.allCoins[ bMarket['MarketCurrencyLong'] ] )
#					hWallet = hw.get_wallet_address( hw.allCoins[ hMarket['MarketCurrencyLong'] ] )
					
#					print( bWallet )
#					print( hWallet )
					
					
#				elif ( ( ( Decimal(hMarket['Last']) / Decimal(bMarket['Ask']) ) - 1 ) * 100 ) > GAIN_PERCENTAGE_THRESHOLD:
#					print( 'Bittrex to HitBTC on Ask > Last' )
#					print( 'Market Currency: ', bMarket['MarketCurrencyLong'] )
#					print( 'Base Currency: ', bMarket['BaseCurrencyLong'] )
#					print( 'Bittrex Market: ', bMarket['Market'] )
#					print( 'HitBTC Market: ', hMarket['Market'] )
#					print( 'Bittrex Volume: ', bMarket['BaseVolume'] )
#					print( 'HitBTC Volume: ', hMarket['BaseVolume'] )
#					print( 'Bittrex Ask: ', bMarket['Ask'] )
#					print( 'HitBTC Last: ', hMarket['Last'] )
#					print( 'Percent gain: ', ( ( Decimal(hMarket['Last']) / Decimal(bMarket['Ask']) ) - 1 ) * 100 )
#					print( '\n\n' )
#					bw.get_all_asks_under_threshold( bMarket['Market'], Decimal(hMarket['Last']) * ( 100 + GAIN_PERCENTAGE_THRESHOLD ), hw.get_all_bids_over_threshold( hMarket['Market'], Decimal(hMarket['Last']) ) )
					
				