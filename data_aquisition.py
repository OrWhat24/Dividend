import yfinance as yf
import pandas as pd
import os

# List of Dividend Kings stock symbols
dividend_kings = ['JNJ', 'PG', 'KO', 'MMM', 'CL', 'TGT', 'MO']  # You can add/remove stocks as needed

# Ensure the stock_data directory exists
if not os.path.exists('stock_data'):
    os.makedirs('stock_data')

# Function to fetch and save stock data
def download_stock_data(symbols, category):
    combined_data = []
    
    for symbol in symbols:
        print(f"Fetching data for {symbol}...")
        data = yf.download(symbol, period="1y")
        data['Symbol'] = symbol
        combined_data.append(data)
        print(f"Data fetched for {symbol}")

    # Combine and save to CSV
    combined_df = pd.concat(combined_data)
    csv_path = f'stock_data/{category}_stock_data.csv'
    combined_df.to_csv(csv_path)
    print(f"CSV saved at: {csv_path}")

# Download data only for Dividend Kings
download_stock_data(dividend_kings, 'Dividend_Kings')
