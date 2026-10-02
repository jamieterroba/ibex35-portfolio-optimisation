import numpy as np
import pandas as pd
import yfinance as yf
from config import asset_file, start_date, end_date

# Download data
tickers = pd.read_csv(asset_file)['ticker'].tolist()
data = yf.download(tickers, start_date, end_date, auto_adjust=True)["Close"].dropna()
num_assets = len(tickers)

# Calculate daily returns of the equities
daily_returns = np.log(data).diff().dropna()
mean_daily_returns = daily_returns.mean()
std_daily_returns = daily_returns.std()
covar_daily_returns = daily_returns.cov()