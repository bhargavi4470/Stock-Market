import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
import yfinance as yf
from datetime import datetime
import time

start = '2015-01-01'
end = '2024-09-29'

# Fix for yfinance download issue - replace this section in your notebook
try:
    # Try direct download first
    df = yf.download('AAPL', start=start, end=end, progress=False)
    if df.empty:
        raise ValueError("Empty dataframe returned")
except Exception as e:
    print(f"Download failed with error: {e}")
    print("Trying alternative method...")
    
    # Method 1: Use ticker object
    try:
        ticker = yf.Ticker('AAPL')
        df = ticker.history(start=start, end=end)
    except:
        # Method 2: Use period parameter
        print("Trying with period parameter...")
        df = yf.download('AAPL', period='10y', interval='1d')
    
    # Method 3: Use shorter period if still failing
    if df.empty:
        print("Trying with 5 year period...")
        df = yf.download('AAPL', period='5y', interval='1d')

# Continue with your existing code...
df = df.reset_index()
df = df.drop(['Date','Adj Close'], axis=1)

# Rest of your existing code continues here...
print("Data download successful!")
print(df.head())
