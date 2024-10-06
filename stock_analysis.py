import pandas_ta as ta
import yfinance as yf

# Download stock data for Apple (AAPL)
data = yf.download("AAPL", start="2023-01-01", end="2024-01-01")

# Calculate MACD using pandas-ta
macd = ta.macd(data['Close'])

# Print the MACD components
print("MACD Values:")
print(macd.tail())
