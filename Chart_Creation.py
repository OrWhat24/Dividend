import os
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

# Ensure the chart directories exist
if not os.path.exists('Charts/Dividend_Kings'):
    os.makedirs('Charts/Dividend_Kings')

# Function to create and save candlestick charts
def create_candlestick_chart(symbol, data):
    # Reset index for mplfinance compatibility
    data.reset_index(inplace=True)
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    
    # Creating candlestick chart with moving averages
    mpf.plot(data, type='candle', mav=(50, 200), volume=True, style='yahoo',
             title=f'{symbol} Stock Price', savefig=f'Charts/Dividend_Kings/{symbol}_chart.png')
    print(f"Chart created for {symbol}")

# Function to process data from CSV
def process_data(category):
    csv_path = f'stock_data/{category}_stock_data.csv'
    
    # Read the CSV file
    if os.path.exists(csv_path):
        data = pd.read_csv(csv_path, parse_dates=True, index_col='Date')
        
        # Group by symbol and create a chart for each stock
        for symbol, group in data.groupby('Symbol'):
            create_candlestick_chart(symbol, group)
    else:
        print(f"CSV file for {category} not found.")

# Process data for Dividend Kings
process_data('Dividend_Kings')
