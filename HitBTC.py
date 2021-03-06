import uuid
import time

import requests
from decimal import *

class HitBTC(object):
    def __init__(self, url, public_key, secret):
        self.url = url + "/api/2"
        self.session = requests.session()
        self.session.auth = (public_key, secret)
		
    def get_currency(self):
        """Get Currency."""
        return self.session.get("%s/public/currency" % (self.url), timeout=5).json()
		
    def get_symbol_all(self):
        """Get symbol."""
        return self.session.get("%s/public/symbol" % (self.url), timeout=5).json()

    def get_symbol(self, symbol_code):
        """Get symbol."""
        return self.session.get("%s/public/symbol/%s" % (self.url, symbol_code), timeout=5).json()
				
    def get_ticker_all(self):
        """Get Tickers."""
        return self.session.get("%s/public/ticker" % (self.url), timeout=5).json()
		
    def get_ticker(self,symbol_code):
        """Get Tickers."""
        return self.session.get("%s/public/ticker/%s" % (self.url, symbol_code),timeout=5).json()

    def get_orderbook(self, symbol_code):
        """Get orderbook. """
        return self.session.get("%s/public/orderbook/%s" % (self.url, symbol_code), timeout=5).json()
		
    def create_address(self, currency_code):
        """Creates new wallet address for desired crypto"""
        return self.session.post("%s/account/crypto/address/%s" % (self.url, currency_code), timeout=5).json()

    def get_address(self, currency_code):
        """Get address for deposit."""
        return self.session.get("%s/account/crypto/address/%s" % (self.url, currency_code), timeout=5).json()

    def get_account_balance(self):
        """Get main balance."""
        return self.session.get("%s/account/balance" % self.url, timeout=5).json()

    def get_trading_balance(self):
        """Get trading balance."""
        return self.session.get("%s/trading/balance" % self.url, timeout=5).json()

    def transfer(self, currency_code, amount, to_exchange):
        return self.session.post("%s/account/transfer" % self.url, data={
                'currency': currency_code, 'amount': amount,
                'type': 'bankToExchange' if to_exchange else 'exchangeToBank'
            }, timeout=5).json()

    def new_order(self, client_order_id, symbol_code, side, quantity, price=None):
        """Place an order."""
        data = {'symbol': symbol_code, 'side': side, 'quantity': quantity}

        if price is not None:
            data['price'] = price

        return self.session.put("%s/order/%s" % (self.url, client_order_id), data=data, timeout=5).json()

    def get_order(self, client_order_id, wait=None):
        """Get order info."""
        data = {'wait': wait} if wait is not None else {}

        return self.session.get("%s/order/%s" % (self.url, client_order_id), params=data, timeout=5).json()

    def cancel_order(self, client_order_id):
        """Cancel order."""
        return self.session.delete("%s/order/%s" % (self.url, client_order_id), timeout=5).json()

    def withdraw(self, currency_code, amount, address, network_fee=None, payment_id=None):
        """Withdraw."""
        data = {'currency': currency_code, 'amount': amount, 'address': address}

        if network_fee is not None:
            data['networkfee'] = network_fee
			
        if payment_id is not None:
            data['paymentId'] = payment_id

        return self.session.post("%s/account/crypto/withdraw" % self.url, data=data, timeout=5).json()

    def get_transaction(self, transaction_id):
        """Get transaction info."""
        return self.session.get("%s/account/transactions/%s" % (self.url, transaction_id), timeout=5).json()