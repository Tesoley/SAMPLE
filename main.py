import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

symbol = "DOGEUSDT"
interval = "1m"
url = f'https://data-api.binance.vision/api/v3/klines?symbol={symbol}&interval={interval}&limit=500'
response = requests.get(url)
hist_data = response.json()

print(hist_data)
