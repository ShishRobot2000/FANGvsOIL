# 📊 Tech vs Oil – Market Analysis and Forecast (2014–2024)

This Python project compares the performance of major American technology companies (FANG++, meaning Facebook/META, Amazon, Netflix, Google/Alphabet, Apple, Microsoft, and Tesla) with that of the world's largest oil corporations (ExxonMobil, Chevron, Shell, BP, and TotalEnergies). The goal is to observe and analyze the historical trend of each stock over a ten-year period, calculate cumulative return, estimate the average growth for each sector, and finally attempt to project the future trend of the two sectors over the next five years using a linear regression model.

The program begins by downloading historical data from January 1st, 2014 to January 1st, 2024 using the `yfinance` library, which allows for retrieving stock prices from Yahoo Finance. For each ticker, the “Adjusted Close” column is selected, and daily percentage returns are calculated. These returns are then cumulatively summed over time to show how much a $1 investment would have grown since the beginning of the period.

Next, two average series are calculated: one for the technology stocks (Tech) and one for the oil stocks (Oil). These curves represent the aggregated trend of the two sectors and allow for a simpler and cleaner comparison compared to individual stocks. The two sectoral averages are then used as a basis for a future forecast. This forecast is based on a simple linear regression, implemented using the `scikit-learn` library, trained on historical data and projected over the following five years (approximately 1260 trading days).

The result of the program is a chart divided into two sections. The first section shows all individual stock trends, both tech and oil, with sectoral averages highlighted. Tech companies are represented with solid lines, oil companies with dashed lines. The second section of the chart displays only the sector averages, accompanied by dashed projected lines: one for the tech average and one for the oil average. This allows for a clear visualization of both past and future performance as estimated by the mathematical models.

To run this script correctly, a few Python libraries are required: `yfinance` for downloading data, `pandas` for data manipulation, `numpy` for numerical calculations, `matplotlib` for generating graphs, and `scikit-learn` for linear regression. These libraries can be installed using `pip` with the following command:

pip install yfinance pandas matplotlib scikit-learn

Once everything is installed, just run the script with:

python fang_vs_oil_forecast.py

The data used comes exclusively from Yahoo Finance and is updated each time the program is run. The tech tickers analyzed are: META, AMZN, NFLX, GOOGL, AAPL, MSFT, and TSLA. The oil tickers are: XOM, CVX, SHEL, BP, and TTE.

The purpose of this project is purely educational: it is intended to explore how to use real financial market data for comparative analysis, build sector indicators, and create simple predictive models. The forecasts made do not in any way constitute financial advice. They are instead an exercise to understand the application of mathematical and statistical tools in the field of quantitative finance.

This project can be expanded in the future with new features, such as risk analysis (volatility, drawdown, Sharpe Ratio), the use of more advanced predictive models like XGBoost or LSTM, or the transformation of the entire system into an interactive web app using Streamlit. Another interesting extension would be to link the system with sentiment analysis based on news or social media, enriching the prediction with exogenous signals.

Created by Pietro Pellegrino – April 2025. All rights reserved. Released under the MIT license.
