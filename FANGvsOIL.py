import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from arch import arch_model
from sklearn.linear_model import LinearRegression

# Step 1. Download historical data up to 3 days ago
fang_tickers = ['META', 'AMZN', 'NFLX', 'GOOGL']
oil_tickers = ['XOM', 'CVX', 'SHEL', 'BP', 'TTE']
all_tickers = fang_tickers + oil_tickers

end_date = pd.Timestamp.today() - pd.Timedelta(days=3)
start_date = '2014-01-01'

print(f"Downloading historical data up to {end_date.strftime('%Y-%m-%d')}...")

data = yf.download(all_tickers, start=start_date, end=end_date.strftime('%Y-%m-%d'), group_by='ticker', auto_adjust=False)
adj_close = pd.DataFrame({ticker: data[ticker]['Adj Close'] for ticker in all_tickers})

# Step 2. Calculate daily returns
returns = adj_close.pct_change().dropna()

# Step 3. Forecast 3 days ahead (Trend + Volatility)
trend_forecasts = {}
volatility_forecasts = {}

# Create figure for all plots
plt.figure(figsize=(18, 12))

plot_index = 1

for ticker in all_tickers:
    print(f"\n📈 Forecasting for {ticker}...")
    ret_series = returns[ticker].dropna()
    
    # Forecast trend with Linear Regression
    X = np.arange(len(ret_series)).reshape(-1, 1)
    y = ret_series.values
    model_lr = LinearRegression()
    model_lr.fit(X, y)
    future_X = np.arange(len(ret_series), len(ret_series) + 3).reshape(-1, 1)
    trend_pred = model_lr.predict(future_X)
    trend_forecasts[ticker] = trend_pred

    # Forecast volatility with GARCH
    model_garch = arch_model(ret_series * 100, vol='Garch', p=1, q=1)
    garch_fit = model_garch.fit(disp='off')
    garch_forecast = garch_fit.forecast(horizon=3)
    volatility_pred = np.sqrt(garch_forecast.variance.iloc[-1])
    volatility_forecasts[ticker] = volatility_pred.values

    # Plotting forecasts
    plt.subplot(4, 3, plot_index)
    plt.plot(range(1, 4), trend_pred * 100, label="Trend forecast (%)", marker='o')
    plt.plot(range(1, 4), volatility_pred, label="Volatility forecast (%)", marker='x')
    plt.title(f"{ticker} - 3 Day Forecast")
    plt.xlabel("Days Ahead")
    plt.ylabel("% Return / Volatility")
    plt.grid(True)
    plt.legend()
    plot_index += 1

plt.suptitle("FANG & OIL - 3-Day Trend and Volatility Forecasts", fontsize=18)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("forecast_fang_oil.png")
print("\n✅ Forecast plots saved as 'forecast_fang_oil.png'.")

# Step 4. Download real stock data (last 3 missing days)
real_start = (pd.Timestamp.today() - pd.Timedelta(days=3)).strftime('%Y-%m-%d')
real_end = pd.Timestamp.today().strftime('%Y-%m-%d')

print(f"\nDownloading real stock data from {real_start} to {real_end}...")

real_data = yf.download(all_tickers, start=real_start, end=real_end, group_by='ticker', auto_adjust=False)
real_adj_close = pd.DataFrame({ticker: real_data[ticker]['Adj Close'] for ticker in all_tickers})

# Step 5. Calculate real returns
real_returns = real_adj_close.pct_change().dropna()

# Step 6. Compare forecast vs real for each stock
print("\n🔍 Comparing Forecast vs Real Returns and Volatility (Over 3 Days)\n")
comparison_table = []

for ticker in all_tickers:
    if ticker not in real_returns.columns:
        print(f"⚠️ No real data for {ticker} — skipping.")
        continue
    
    real_ret = real_returns[ticker].values[:3]  # Real returns (next 3 days)
    pred_ret = trend_forecasts[ticker]
    pred_vol = volatility_forecasts[ticker]
    
    # Save comparison
    for i in range(len(real_ret)):
        comparison_table.append({
            'Ticker': ticker,
            'Day': i + 1,
            'Predicted Return (%)': round(pred_ret[i] * 100, 3),
            'Real Return (%)': round(real_ret[i] * 100, 3),
            'Predicted Volatility (%)': round(pred_vol[i], 3),
            'Real Volatility Approx (%)': round(abs(real_ret[i]) * 100, 3)
    })

# Convert to DataFrame
comparison_df = pd.DataFrame(comparison_table)

# Print nicely
print(comparison_df.to_string(index=False))

# Save results
comparison_df.to_csv("forecast_vs_real_results.csv", index=False)
print("\n✅ Results saved to 'forecast_vs_real_results.csv'.")
