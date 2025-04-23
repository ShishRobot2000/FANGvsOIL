import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Define stock tickers
tech_tickers = ['META', 'AMZN', 'NFLX', 'GOOGL', 'AAPL', 'MSFT', 'TSLA']
oil_tickers = ['XOM', 'CVX', 'SHEL', 'BP', 'TTE']
tickers = tech_tickers + oil_tickers

# Download stock data from Yahoo Finance
data = yf.download(tickers, start='2014-01-01', end='2024-01-01', group_by='ticker', auto_adjust=False)
adj_close = pd.DataFrame({ticker: data[ticker]['Adj Close'] for ticker in tickers})

# Calculate cumulative returns
returns = adj_close.pct_change().fillna(0)
cumulative = (1 + returns).cumprod()

# Compute sector averages
cumulative['TECH_MEAN'] = cumulative[tech_tickers].mean(axis=1)
cumulative['OIL_MEAN'] = cumulative[oil_tickers].mean(axis=1)

# Linear regression forecast function
def predict(series, days=252*5):
    X = np.arange(len(series)).reshape(-1, 1)
    y = series.values
    model = LinearRegression()
    model.fit(X, y)
    future_X = np.arange(len(series) + days).reshape(-1, 1)
    y_pred = model.predict(future_X)
    return y_pred

# Forecast for the next 5 years
tech_pred = predict(cumulative['TECH_MEAN'])
oil_pred = predict(cumulative['OIL_MEAN'])
dates = pd.date_range(start=cumulative.index[0], periods=len(tech_pred), freq='B')

# Plotting the results
plt.figure(figsize=(14, 10))

# Plot 1: All stocks + sector averages
plt.subplot(2, 1, 1)
for t in tech_tickers:
    plt.plot(cumulative[t], linewidth=1, label=f'Tech: {t}')
for t in oil_tickers:
    plt.plot(cumulative[t], linestyle='--', linewidth=1, label=f'Oil: {t}')
plt.plot(cumulative['TECH_MEAN'], color='black', linewidth=3, label='📱 Tech Avg')
plt.plot(cumulative['OIL_MEAN'], color='gray', linewidth=3, linestyle='--', label='🛢️ Oil Avg')
plt.title('Cumulative Returns – All Stocks (2014–2024)')
plt.legend(ncol=2, fontsize=8)
plt.grid()

# Plot 2: Sector averages + forecast
plt.subplot(2, 1, 2)
plt.plot(cumulative['TECH_MEAN'], label='📱 Tech Historical', color='black')
plt.plot(cumulative['OIL_MEAN'], label='🛢️ Oil Historical', color='gray')
plt.plot(dates, tech_pred, '--', label='📈 Tech Forecast (5y)', color='black')
plt.plot(dates, oil_pred, '--', label='📉 Oil Forecast (5y)', color='gray')
plt.title('5-Year Forecast – Sector Averages (Linear Regression)')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()

