# project SAMPLE

git init\
git add README.md \ 
git commit -m "first commit" \
git branch -M main \
git remote add origin https://github.com/Tesoley/SAMPLE.git \
git push -u origin main



використовуємо документацію Websocket library https://developers.binance.com/en/docs/products/spot/web-socket-streams

download the lib \
pip install websocket-client

websocket documentation : https://websocket-client.readthedocs.io/en/latest/

copied from documentation:
```
ws = websocket.WebSocketApp("wss://api.gemini.com/v1/marketdata/BTCUSD",
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close)
```
