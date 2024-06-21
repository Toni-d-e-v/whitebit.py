# WhiteBit SDK for Python
This is a wrapper for the WhiteBit API.

## Requirements
requests

## Quickstart
1. Download `client.py`
```python
import client

api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'
api_url = "https://whitebit.com"

client = WhiteBit(api_key, api_secret, api_url)
print(client.get_ticker())
```
### Public API Functions

- `get_ticker`
  - No parameters required

- `get_assets`
  - No parameters required

- `get_order_book`
  - Parameters:
    - `market` (required)
    - `optimal` (optional)
    - `limit` (optional)
    - `level` (optional)

- `get_trades`
  - Parameters:
    - `market` (required)
    - `type` (optional, values: `buy`/`sell`)

- `get_collateral_markets`
  - No parameters required

- `get_fee`
  - No parameters required

- `get_servertime`
  - No parameters required

### Private API Functions

- `get_balance`
  - No parameters required

- `get_deposit_address`
  - Parameters:
    - `currency` (required)
    - `network` (required)

- `withdraw`
  - Parameters:
    - `ticker` (required)
    - `amount` (required)
    - `address` (required)
    - `network` (required)
    - `unique_id` (required)
    - `memo` (optional)

- `transfer_balance`
  - Parameters:
    - `from` (required)
    - `to` (required)
    - `amount` (required)
    - `network` (required)

- `get_trade_balance`
  - No parameters required

- `new_order_limit`
  - Parameters:
    - `side` (required)
    - `amount` (required)
    - `price` (required)
    - `market` (required)

- `new_order_market`
  - Parameters:
    - `side` (required)
    - `amount` (required)
    - `price` (required)
    - `market` (required)

- `cancel_order`
  - Parameters:
    - `order_id` (required)
    - `market` (required)

- `get_orders`
  - Parameters:
    - `market` (required)

- `get_order`
  - Parameters:
    - `order_id` (required)
    - `market` (required)
