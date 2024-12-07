# 07.12.2024
# yfinance only for USA Stock -> sad

import yfinance as yf

ticker_symbol = '3CP'

ticker = yf.Ticker(ticker_symbol)

historical_data = ticker.history(period='1mo')

print(f'Summary of Historical Data for {ticker_symbol}:')
print(historical_data[['Open', 'High', 'Low', 'Close', 'Volume']])