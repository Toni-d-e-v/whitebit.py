# WhiteBit SDK for Python
This is a wrapper for WhiteBit api.
## Requirements
```
requests
```
# Quickstart
- Download client.py 
```
import client
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'
api_url = "https://whitebit.com"
clinet = WhiteBit(api_key,api_secret,api_url)
print(clinet.get_ticker())
```
# Functions

## Public Api
Public Api SDK functions
### get_ticker
This function retrieves a 24-hour pricing and volume summary for each market pair available on the exchange.
```
{
  "BTC_USDT": {
    "base_id": 1,                           // CoinmarketCap Id of base currency; 0 - if unknown
    "quote_id": 825,                        // CoinmarketCap Id of quote currency; 0 - if unknown
    "last_price": "9164.09",                // Last price
    "quote_volume": "43341942.90416876",    // Volume in quote currency
    "base_volume": "4723.286463",           // Volume in base currency
    "isFrozen": false,                      // Identifies if trades are closed
    "change": "0.57"                        // Change in percent between open and last prices
  },
  {...}
}
```
### get_assets
This function retrieves a retrieves the assets status.
```
{
  "BTC": {
    "name": "Bitcoin",                        // Full name of cryptocurrency.
    "unified_cryptoasset_id": 1,              // Unique ID of cryptocurrency assigned by Unified Cryptoasset ID, 0 if unknown
    "can_withdraw": true,                     // Identifies whether withdrawals are enabled or disabled.
    "can_deposit": true,                      // Identifies whether deposits are enabled or disabled.
    "min_withdraw": "0.001",                  // Identifies the single minimum withdrawal amount of a cryptocurrency.
    "max_withdraw": "2",                      // Identifies the single maximum withdrawal amount of a cryptocurrency.
    "maker_fee": "0.1",                       // Maker fee in percentage
    "taker_fee": "0.1",                       // Taker fee in percentage
    "min_deposit": "0.0001",                  // Min deposit amount
    "max_deposit": "0",                       // Max deposit amount, will not be returned if there is no limit, 0 if unlimited
    "currency_precision": 18,                 // Max number of digits to the right of the decimal point
    "is_memo": false,                         // Identifies if currency has memo address
    "networks": {                             // Currency networks. It might be a list of networks for cryptocurrency networks or just a single item list for simple cryptocurrencies or tokens
      "deposits": [                           // Networks available for depositing
        "BTC"
      ],
      "withdraws": [                          // Networks available for withdrawing
        "BTC"
      ],
      "default": "BTC"                        // Default network for depositing / withdrawing if available
    },
    "limits": {                               // Currency limits by each network
      "deposit": {                            // Deposits limits
        "BTC": {                              // Network
          "min": "0.001"                      // Max deposit amount
        },
      },
      "withdraw": {                           // Withdraws limits
        "BTC": {                              // Network
          "min": "0.002",                     // Min withdraw amount
        },
      }
    }
  },
  "ETH": {
```
### get_order_book args: market optimal: limit level
This function retrieves the current order book as two arrays (bids / asks) with additional parameters.
```
{
  "timestamp": 1594391413,        // Current timestamp
  "asks": [                       // Array of ask orders
    [
      "9184.41",                  // Price of lowest ask
      "0.773162"                  // Amount of lowest ask
    ],
    [ ... ]
  ],
  "bids": [                       // Array of bid orders
    [
      "9181.19",                  // Price of highest bid
      "0.010873"                  // Amount of highest bid
    ],
    [ ... ]
  ]
}
```
### get_trades args: market type: buy/sell 
This function retrieves the last trades for a given market.
```
[
  {
    "tradeID": 158056419,             // A unique ID associated with the trade for the currency pair transaction Note: Unix timestamp does not qualify as trade_id.
    "price": "9186.13",               // Transaction price in quote pair volume.
    "quote_volume": "0.0021",         // Transaction amount in quote pair volume.
    "base_volume": "9186.13",         // Transaction amount in base pair volume.
    "trade_timestamp": 1594391747,    // Unix timestamp in milliseconds, identifies when the transaction occurred.
    "type": "sell"                    // Used to determine whether or not the transaction originated as a buy or sell. Buy – Identifies an ask that was removed from the order book. Sell – Identifies a bid that was removed from the order book.
  },
  {
    "tradeID": 158056416,
    "price": "9186.13",
    "base_volume": "9186.13",
    "quote_volume": "0.002751",
    "trade_timestamp": 1594391746,
    "type": "sell"
  },
  {...}
}
```
### get_collateral_markets
This function retrieves the collateral markets.
```
[
    "ADA_USDT",
    "BCH_USDT",
    "BTC_USDT",
    "DOGE_USDT",
    "EOS_USDT",
    "ETH_BTC",
    "ETH_USDT",
    "LINK_USDT",
    "LTC_USDT",
    "SHIB_USDT",
    "SOL_USDT",
    "TRX_USDT",
    "USDC_USDT",
    "XLM_USDT",
    "XRP_USDT"
]
```
### get_fee
This function  retrieves the list of fees and min/max amount for deposits and withdraws
```
{
  "USDT (ERC20)": {
    "ticker": "USDT",                         // currency ticker
    "name": "Tether US",                      // currency ticker
    "providers": [],
    "deposit": {                              // deposit fees
      "min_amount": "0.0005",                 // min deposit amount. 0 if there is no limitation
      "max_amount": "0.1",                    // max deposit amount. 0 if there is no limitation
      "fixed": "0.0005",                      // fixed fee amount which applies for all transaction
      "flex": {
        "min_fee": "100",                     // min fee amount
        "max_fee": "1000",                    // max fee amount
        "percent": "10"
      },                                      // flex fee only applies for all transactions but according to min/max fee. Nullable if there is no flex fee
    },
    "withdraw": {
      "min_amount": "0.001",
      "max_amount": "0",
      "fixed": null,
      "flex": null
    },
    "is_depositable": true,                   //true if currency can be deposit
    "is_withdrawal": true                     //true if currency can be withdraw
  },
```
### get_servertime
This function retrieves the current server time.
```
{
  "time": 1631451591
}
```
## Private Api
Private Api SDK functions
### get_balance
This function retrieves the balance.
```
{
    "BSV": {
        "main_balance": "0"           // main balance volume of BSV
    },
    "BTC": {
        "main_balance": "0"           // main balance volume of BTC
    },
    "BTG": {
        "main_balance": "0"           // main balance volume of BTG
    },
    "BTT": {
        "main_balance": "0"           // main balance volume of BTT
    },
    "XLM": {
        "main_balance": "36.48"       // main balance volume of XLM
    },
    "currecty_ticker": {...}
}
```

### get_deposit_address args: currency network
This function retrieves the deposit address for a given currency and network.
```
{
    "account": {
        "address": "GDTSOI56XNVAKJNJBLJGRNZIVOCIZJRBIDKTWSCYEYNFAZEMBLN75RMN",        // deposit address
        "memo": "48565488244493"                                                      // memo if currency requires memo
    },
    "required": {
        "fixedFee": "0",                                                              // fixed deposit fee
        "flexFee": {                                                                  // flexible fee - is fee that use percent rate
            "maxFee": "0",                                                            // maximum fixed fee that you will pay
            "minFee": "0",                                                            // minimum fixed fee that you will pay
            "percent": "0"                                                            // percent of deposit that you will pay
        },
        "maxAmount": "0",                                                             // max amount of deposit that can be accepted by exchange - if you deposit more than that number, it won't be accepted by exchange
        "minAmount": "1"                                                              // min amount of deposit that can be accepted by exchange - if you will deposit less than that number, it won't be accepted by exchange
    }
}
```
### withdraw args: ticker amount address network unique_id optimal: memo
This function withdraws funds to a given address.
- Response: Available statuses:
    - Status 201 if validation succeeded and withdraw creation process is started
    - Status 400 if request validation failed
    - Status 422 if inner validation failed
### transfer_balance args: from to amount network
This function transfers the specified amount between main and trade balances
- Response: Available statuses:
    - Status 201 if validation succeeded and withdraw creation process is started
    - Status 400 if request validation failed
    - Status 422 if inner validation failed
### get_trade_balance
This function retrieves the trade balance.
- Available statuses:
  - Status 200
  -  Status 422 if request validation failed
  -  Status 400 if inner validation failed
  -  Status 503 if service temporary unavailable
### new_order_limit args: side amount price market
This function creates a new limit order.
- Response: Available statuses:

  -  Status 200
  -  Status 400 if inner validation failed
  -  Status 422 if request validation failed
  -  Status 503 if service temporary unavailable
### new_order_market args: side amount price market
This function creates a new market order.
- Response: Available statuses:
  -  Status 200
  -  Status 400 if inner validation failed
  -  Status 422 if request validation failed
  -  Status 503 if service temporary unavailable
### cancel_order args: order_id market
This function cancels an order.
- Available statuses:
-  Status 200
-    Status 400 if inner validation failed
-    Status 422 if validation failed
-    Status 503 if service temporary unavailable
### get_orders args: market 
This function retrieves the list of orders.
- Available statuses:
-  Status 200
-    Status 400 if inner validation failed
-    Status 422 if validation failed
-    Status 503 if service temporary 
### get_order args: order_id market
This function retrieves the order details.
- Available statuses:
-  Status 200
-    Status 400 if inner validation failed
-    Status 422 if validation failed
-    Status 503 if service temporary 