import requests as requests
import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt

symbol = "DOGEUSDT"
interval = "1m"
url = f'https://data-api.binance.vision/api/v3/klines?symbol={symbol}&interval={interval}&limit=500'
response = requests.get(url)
hist_data = response.json()

df = pd.DataFrame(
    hist_data,
    columns=[
        "open_time",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "close_time",
        "quote_volume",
        "trades_count",
        "taker_buy_base",
        "taker_buy_quote",
        "ignore",
    ],
)

df = df.drop(columns=["ignore"])
print(df)
print(df.shape)
print(df.info())
