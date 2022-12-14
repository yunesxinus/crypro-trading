# for more details see here: https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md#live-subscribingunsubscribing-to-streams

import json
# pretty-print
from pprint import pprint

import pandas as pd
import pandas_ta as ta
import ccxt
from websocket import WebSocketApp

symbol = 'btcusdt'
second_symbol = 'ethusdt'
interval = '1m'

'''
wss: protocol
stream.binance.com: host
9443: port
ws/symbol@kline_interval: path
'''
url = f'wss://stream.binance.com:9443/ws/{symbol}@kline_{interval}'


counter = 0

# for more details about `websocket-client` see https://websocket-client.readthedocs.io/en/latest/examples.html


def websocket_on_open(ws: WebSocketApp, *args, **kwargs):
    print('websocket opened')


def websocket_on_close(ws: WebSocketApp, *args, **kwargs):
    print('websocket closed')

# important!, when server send any data, you got it here (means you can process it!)


def websocket_on_message(ws: WebSocketApp, message: str, *args, **kwargs):
    global counter

    json_message = json.loads(str(message))

    print(f'{counter}) new message ->', end=' ')
    pprint(json_message)

    # subscribe to new symbol
    if counter == 5:
        print(f'also subscribe to {second_symbol}')
        payload = {
            'method': 'SUBSCRIBE',
            'params': [
                f'{second_symbol}@kline_{interval}',
            ],
            'id': 1
        }

        # send data to server via ws object (send data to server with WebSocket not RESTful API!)
        ws.send(
            # convert dictionary to string
            json.dumps(payload)
        )

    # unsubscribe first symbol
    elif counter == 15:
        print(f'unsubscribe to {second_symbol}')
        payload = {
            'method': 'UNSUBSCRIBE',
            'params': [
                f'{symbol}@kline_{interval}',
            ],
            'id': 1
        }

        # send data to server via ws object (send data to server with WebSocket not RESTful API!)
        ws.send(
            # convert dictionary to string
            json.dumps(payload)
        )

    # disconnect websocket (means kill websocket)
    elif counter == 20:
        ws.close()

    counter += 1


# create websocket object
ws = WebSocketApp(url, on_open=websocket_on_open,
                  on_close=websocket_on_close,
                  on_message=websocket_on_message)

# connect to server then run! easy peasy lemon squeezy :)))
ws.run_forever()
# "e": "1hTicker",    // Event type
#   "E": 123456789,     // Event time
#   "s": "BNBBTC",      // Symbol
#   "p": "0.0015",      // Price change
#   "P": "250.00",      // Price change percent
#   "o": "0.0010",      // Open price
#   "h": "0.0025",      // High price
#   "l": "0.0010",      // Low price
#   "c": "0.0025",      // Last price
#   "w": "0.0018",      // Weighted average price
#   "v": "10000",       // Total traded base asset volume
#   "q": "18",          // Total traded quote asset volume
#   "O": 0,             // Statistics open time
#   "C": 86400000,      // Statistics close time
#   "F": 0,             // First trade ID
#   "L": 18150,         // Last trade Id
#   "n": 18151          // Total number of trades
