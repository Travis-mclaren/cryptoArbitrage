from decimal import *
	
	
def get_actual_profit( quantity, askPrice, takerFee, bidPrice, makerFee, txFee, btcToUsdValue ):
	return ( ( (Decimal(quantity) - Decimal(txFee)) * Decimal(bidPrice) * Decimal(makerFee) ) - ( Decimal(quantity) * Decimal(askPrice) * Decimal(takerFee) ) ) * Decimal(btcToUsdValue)
	
	
def get_profit_percentage( quantity, askPrice, takerFee, bidPrice, makerFee, txFee ):
	return ( ( (Decimal(quantity) - Decimal(txFee)) * Decimal(bidPrice) * Decimal(makerFee) ) - ( Decimal(quantity) * Decimal(askPrice) * Decimal(takerFee) ) )
	
def lowest_profitable_trade( quantity, askPrice, takerFee, bidPrice, makerFee, txFee ):
	x = 0
	while x < quantity:
		x += 1
		if get_profit_percentage( x, askPrice, takerFee, bidPrice, makerFee, txFee ) > 0:
			break
	
	return x