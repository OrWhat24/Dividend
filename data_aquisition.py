import yfinance as yf
import pandas as pd
import os

# Lists of Dividend Kings, Aristocrats, and Contenders stock symbols
dividend_kings = ['JNJ', 'PG', 'KO', 'MMM', 'CL', 'TGT', 'MO']  # Add more symbols
dividend_aristocrats = ['ABBV', 'XOM', 'T', 'CVX']  # Add more symbols
dividend_contenders = ['AFL', 'AOS', 'BKH', 'CWT']  # Add more symbols

# Directory to save the data
data_dir = "stock_data"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Function to download stock data and save as CSV
def download_stock_data(stock_list, category_name):
    combined_data = []
    for symbol in stock_list:
        print(f"Fetching data for {symbol}...")
        # Fetch stock data for the last year
        data = yf.download(symbol, period="1y", interval="1d")
        
        # Check if data was fetched correctly
        if not data.empty:
            print(f"Data fetched for {symbol}")
            data['Symbol'] = symbol  # Add a column to keep track of the symbol
            combined_data.append(data)
        else:
            print(f"No data found for {symbol}")
    
    # Combine all data into a single DataFrame
    if combined_data:
        combined_df = pd.concat(combined_data, ignore_index=False)
        file_path = os.path.join(data_dir, f"{category_name}_stock_data.csv")
        combined_df.to_csv(file_path)
        print(f"CSV saved at: {file_path}")
    else:
        print(f"No data to save for {category_name}")

# Download and save data for each category
download_stock_data(dividend_kings, 'Dividend_Kings')
download_stock_data(dividend_aristocrats, 'Dividend_Aristocrats')
download_stock_data(dividend_contenders, 'Dividend_Contenders')
