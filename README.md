# 📊 FANG vs OIL – Trend and Volatility Forecasting (Short-Term Focus)

## 🛠️ Project Overview

This project analyzes and forecasts the short-term behavior of two major sectors:

- 📱 FANG stocks: META, AMZN, NFLX, GOOGL
- 🛢️ Oil stocks: XOM, CVX, SHEL, BP, TTE

We initially compared long-term performance (5 years) but later **refined the scope to a short-term (3 days) prediction**, focusing separately on:

- **Trend prediction** (returns forecast)
- **Volatility prediction** (risk forecast)

---

## 📈 First Attempt: ARIMA Model

At the beginning of the project, we tried to apply a classic **ARIMA(1,1,1)** model on the cumulative returns of the sectors.

- We aimed to **forecast 5 years ahead**.
- However, ARIMA proved **unsuitable** for this financial context:
  - The forecasted series were **almost flat**.
  - ARIMA assumes a stable and slowly evolving process, while financial returns are much more **random and volatile**.
  - In finance, the **variance** (volatility) matters more than the absolute level of returns.

Thus, **ARIMA was abandoned** for this specific goal.

---

## 🔥 New Strategy: GARCH Model + Short-Term Horizon

We redesigned the project using a more **financially appropriate approach**:

- **Forecasting Volatility**: Using **GARCH(1,1)** models, which are perfect to model financial time series with **changing variance**.
- **Forecasting Trend**: Using a **Linear Regression** model to predict short-term directional movements.
- **Short-Term Forecast**: Instead of 5 years, we focused on the **next 3 business days** to reflect more realistic market dynamics.

---

## 📋 What the project does:

1. **Download stock data** up to three business days ago.
2. **Calculate daily returns**.
3. For each stock individually:
   - **Fit a GARCH(1,1) model** to forecast 3-day volatility.
   - **Fit a Linear Regression model** to forecast 3-day trend.
4. **Download real stock data** for the last 3 business days.
5. **Compare** the forecasts against the real observed data:
   - Predicted returns vs Real returns
   - Predicted volatility vs Realized volatility
6. **Save all results**:
   - Combined forecasts in a single PNG file (`forecast_fang_oil.png`).
   - Final comparison table in a CSV file (`forecast_vs_real_results.csv`).

---

## 📦 Requirements

- Python 3.8+
- Packages:
  - `yfinance`
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `arch`
  - `scikit-learn`

Install everything with:

```bash
pip install yfinance pandas matplotlib numpy arch scikit-learn
```

---

## 📁 Output Files

- `forecast_fang_oil.png`: Visualization of trend and volatility forecasts for all stocks.
- `forecast_vs_real_results.csv`: Table comparing predicted vs real returns and volatilities over the next 3 days.

---

## 🎯 Conclusion

This project shows the **importance of choosing the right forecasting model** based on the nature of the data:

- Long-term financial forecasting is unreliable without modeling volatility.
- **Short-term, volatility-driven forecasting** (like GARCH) gives more meaningful insights into stock behavior.
- **Comparing predictions with real results** strengthens model evaluation and improves understanding of financial dynamics.

---

## ⚠️ Disclaimer

This project is developed solely for **learning and educational purposes**.  
It does **not** provide financial advice, stock recommendations, or investment guidance.

---

_Developed and programmed by Pietro Pellegrino — April 2025_  
_License: MIT_
