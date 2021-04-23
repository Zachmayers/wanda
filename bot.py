# https://www.youtube.com/watch?v=GdlFhF6gjKo&t=404s&ab_channel=PartTimeLarry

import websocket, json, pprint

SOCKET = "wss://stream.binance.com:9443/ws/dogeusdt@kline_1m"
RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
TRADE_SYMBOL = 'DOGEUSD'
TRADE_QUANTITY = 10


closes = []
in_position = False

def on_open(ws):
    print('opened connection')

def on_close(ws):
    print('closed connection')

def on_message(ws, message):
    global closes, in_position
    
    print('received message')
    json_message = json.loads(message)
    pprint.pprint(json_message)

    candle = json_message['k']

    # is_candle_closed = candle['x']
    # close = candle['c']

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()