import json
import base64
import requests
import time
import hmac
import hashlib

class WhiteBit:
    def __init__(self,api_key,secret_key,url):
        self.api_key = api_key
        self.secret_key = secret_key
        self.nonce = str(int(time.time()))
        self.baseUrl = url
    
    def send_request_post(self,data,completeUrl):
        data_json = json.dumps(data, separators=(',', ':'))
        payload = base64.b64encode(data_json.encode('ascii'))
        signature = hmac.new(self.secret_key.encode('ascii'), payload, hashlib.sha512).hexdigest()
        headers = {
            'Content-type': 'application/json',
            'X-TXC-APIKEY': self.api_key,
            'X-TXC-PAYLOAD': payload,
            'X-TXC-SIGNATURE': signature,
        }
        resp = requests.post(completeUrl, headers=headers, data=data_json)
        return resp.json()
    
    def send_request_get(self,completeUrl):
        headers = {
            'X-TXC-APIKEY': self.api_key
        }
        resp = requests.get(completeUrl, headers=headers)
        return resp.json()

    def get_ticker(self):
        completeUrl = self.baseUrl + '/api/v4/public/ticker'
        return self.send_request_get(completeUrl)

    def get_assets(self):
        completeUrl = self.baseUrl + '/api/v4/public/assets'

        return self.send_request_get(completeUrl)
    def get_order_book(self,market,limit=100,level=2):
        completeUrl = self.baseUrl + '/api/v4/public/orderbook/' + market + '?limit=' + str(limit) + '&level=' + str(level)
        return  self.send_request_get(completeUrl)

    def get_trades(self,market,type='sell'):
        completeUrl = self.baseUrl + '/api/v4/public/trades/' + market + '?type=' + type
        return  self.send_request_get(completeUrl)

    def get_collateral_markets(self):
        completeUrl = self.baseUrl + '/api/v4/public/collateral/markets'
        return self.send_request_get(completeUrl)

    def get_fee(self):
        completeUrl = self.baseUrl + '/api/v4/public/fee'
        return  self.send_request_get(completeUrl)

    def get_servertime(self):
        completeUrl = self.baseUrl + '/api/v4/public/time'
        return  self.send_request_get(completeUrl)

    # PRIVATE API

    # [POST] /api/v4/main-account/balance
    def get_balance(self):
        data = {
            'request': '/api/v4/main-account/balance'
        }
        completeUrl = self.baseUrl + '/api/v4/main-account/balance'
        return self.send_request_post(data,completeUrl)

    # [POST] /api/v4/main-account/address
    # This endpoint retrieves a deposit address of the cryptocurrency.
    def get_deposit_address(self,currency,network):
        data = {
            'request': '/api/v4/main-account/address',
            'ticker': currency,
            'network': network
        }
        completeUrl = self.baseUrl + '/api/v4/main-account/address'
        return self.send_request_post(data,completeUrl)

    # [POST] /api/v4/main-account/withdraw
    # This endpoint creates withdraw for the specified ticker.
    # memo is optional if its required for the cryptocurrency.
    def withdraw(self,ticker,amount,address,network,uniqueId,memo=None):
        if memo is None:
            data = {
                'request': '/api/v4/main-account/withdraw',
                'ticker': ticker,
                'amount': amount,
                'address': address,
                'network': network,
                'uniqueId': uniqueId
            }
        else:
            data = {
                'request': '/api/v4/main-account/withdraw',
                'ticker': ticker,
                'amount': amount,
                'address': address,
                'network': network,
                'uniqueId': uniqueId,
                'memo': memo
            }
        completeUrl = self.baseUrl + '/api/v4/main-account/withdraw'
        return self.send_request_post(data,completeUrl)
    
    #[POST] /api/v4/main-account/transfer
    # This endpoint transfers the specified amount between main and trade balances
    # from - Balance FROM which funds will move to. Acceptable values: main, spot, collateral
    # to - Balance TO which funds will move from. Acceptable values: main, spot, collateral
    # ticker
    # amount
    def transfer_balance(self,_from,to,ticker,amount):
        data = {
            'request': '/api/v4/main-account/transfer',
            'from': _from,
            'to': to,
            'ticker': ticker,
            'amount': amount
        }
        completeUrl = self.baseUrl + '/api/v4/main-account/transfer'
        return self.send_request_post(data,completeUrl)

    # [POST] /api/v4/trade-account/balance
    def get_trade_balance(self):
        data = {
            'request': '/api/v4/trade-account/balance'
        }
        completeUrl = self.baseUrl + '/api/v4/trade-account/balance'
        return self.send_request_post(data,completeUrl)



    def new_order_limit(self,side,amount,price,market):
        data = {
            'market': market,
            'side': side,
            'amount': amount,
            'price': price,
            'request': '/api/v4/order/new'
        }
        completeUrl = self.baseUrl + '/api/v4/order/new'
        return self.send_request_post(data,completeUrl)
    # [POST] /api/v4/order/market
    def new_order_market(self,side,amount,market):
        data = {
            'market': market,
            'side': side,
            'amount': amount,
            'request': '/api/v4/order/market'
        }
        completeUrl = self.baseUrl + '/api/v4/order/market'
        return self.send_request_post(data,completeUrl)
    
    # [POST] /api/v4/order/cancel
    # market, orderid
    def cancel_order(self,market,orderid):
        data = {
            'market': market,
            'orderid': orderid,
            'request': '/api/v4/order/cancel'
        }
        completeUrl = self.baseUrl + '/api/v4/order/cancel'
        return self.send_request_post(data,completeUrl)
    # [POST] /api/v4/orders
    # This endpoint retrieves unexecuted orders only.
    # market = mandatory yes
    def get_orders(self,market):
        data = {
            'market': market,
            'request': '/api/v4/orders'
        }
        completeUrl = self.baseUrl + '/api/v4/orders'
        return self.send_request_post(data,completeUrl)
    # [POST] /api/v4/orders
    def get_order(self,market,orderid):
        data = {
            'market': market,
            'orderid': orderid,
            'request': '/api/v4/order'
        }
        completeUrl = self.baseUrl + '/api/v4/order'
        return self.send_request_post(data,completeUrl)
