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
