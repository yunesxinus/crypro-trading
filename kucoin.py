import json
from kucoin.client import Client

api_key = '63165975664c390001a2b377'
api_secret = 'a2f47d0c-87df-42f6-b778-ad3bbce2b997'
api_passphrase = config.PASSPHRASE

client = Client(api_key, api_secret, api_passphrase)
x = client.get_ticker('BTC-USDT')
