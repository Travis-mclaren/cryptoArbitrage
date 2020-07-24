from decimal import *

getcontext().prec = 8

class Market:

	def __init__( self, exchange, market, bid, ask, last, high, low ):
		self.toCurrency			= toCurrency
		self.toCurrencyLong		= toCurrencyLong
		self.fromCurrency		= fromCurrency
		self.fromCurrencyLong	= fromCurrencyLong
		self.bid				= Decimal( bid )
		self.ask				= Decimal( ask )
		self.last				= Decimal( last )
		self.high				= Decimal( high )
		self.low				= Decimal( low )
		
		return
		
	def __str__( self ):
		return (  str( self.market ) 					+ ','
				+ str( self.hitBTCMarket )				+ ','
				+ str( format( self.bid		, '.8f' ) ) + ','
				+ str( format( self.ask		, '.8f' ) ) + ',' 
				+ str( format( self.last	, '.8f' ) ) + ','
				+ str( format( self.high	, '.8f' ) ) + ','
				+ str( format( self.low		, '.8f' ) ) + '\n' )