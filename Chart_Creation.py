import pandas as pd
import matplotlib.pyplot as plt
import os
import talib as ta
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.ticker as mticker

# Define the directories for the CSV data and chart output
data_dir = "stock_data"
output_dirs = {
    'Dividend_Kings': "Kings_Charts",
    'Dividend_Aristocrats': "Aristocrat_Charts",
    'Dividend_Contenders': "Contenders_Charts"
}

# Ensure output directories exist
for folder in output_dirs.values():
    if not os.path.exists(folder):
        os.makedirs(folder)

# Function to create candlestick chart with MACD, Stochastics, and Moving Averages
def create_candlestick_macd_stochastic_chart(data, symbol, category):
    # Convert dates for candlestick plotting
    data['Date'] = pd.to_datetime(data.index)
    data['Date'] = mdates.date2num(data['Date'])

    # Calculate 50-day and 200-day moving averages
    data['MA50'] = ta.SMA(data['Close'], timeperiod=50)
    data['MA200'] = ta.SMA(data['Close'], timeperiod=200)

    # Create the figure and the subplots
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(10, 10), gridspec_kw={'height_ratios': [2, 1, 1, 1]})

    # --- Candlestick Chart with Moving Averages ---
    ohlc = data[['Date', 'Open', 'High', 'Low', 'Close']].copy()
    candlestick_ohlc(ax1, ohlc.values, width=0.6, colorup='green', colordown='red', alpha=0.8)

    # Plot 50-day and 200-day moving averages
    ax1.plot(data.index, data['MA50'], label='50-Day MA', color='orange', linewidth=2)
    ax1.plot(data.index, data['MA200'], label='200-Day MA', color='purple', linewidth=2)

    # Set title and axis formats
    ax1.set_title(f'{symbol} Candlestick Chart with MACD, Stochastics, and Moving Averages')
    ax1.xaxis_date()
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.legend()

    # --- MACD ---
    macd, macd_signal, macd_hist = ta.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    ax2.plot(data.index, macd, label='MACD', color='blue')
    ax2.plot(data.index, macd_signal, label='Signal Line', color='orange')
    ax2.bar(data.index, macd_hist, label='MACD Histogram', color='grey')
    ax2.set_ylabel('MACD')
    ax2.legend()

    # --- Fast Stochastic ---
    fast_k, fast_d = ta.STOCH(data['High'], data['Low'], data['Close'], fastk_period=5, slowk_period=3, slowd_period=3)
    ax3.plot(data.index, fast_k, label='Fast %K', color='blue')
    ax3.plot(data.index, fast_d, label='Fast %D', color='red')
    ax3.set_ylabel('Fast Stochastics')
    ax3.legend()

    # --- Slow Stochastic ---
    slow_k, slow_d = ta.STOCH(data['High'], data['Low'], data['Close'], fastk_period=14, slowk_period=3, slowd_period=3)
    ax4.plot(data.index, slow_k, label='Slow %K', color='blue')
    ax4.plot(data.index, slow_d, label='Slow %D', color='red')
    ax4.set_ylabel('Slow Stochastics')
    ax4.legend()

    # Adjust layout and save the plot
    plt.tight_layout()
    output_path = os.path.join(output_dirs[category], f'{symbol}_candlestick_macd_stochastic_chart.png')
    plt.savefig(output_path)
    plt.close()
    print(f"Candlestick chart with MACD and Stochastics for {symbol} saved in {output_dirs[category]}.")

# Function to process the CSV files and create charts
def process_data(category):
    csv_file = os.path.join(data_dir, f"{category}_stock_data.csv")
    data = pd.read_csv(csv_file, parse_dates=True, index_col='Date')
    
    # Get unique stock symbols from the data
    symbols = data['Symbol'].unique()

    for symbol in symbols:
        symbol_data = data[data['Symbol'] == symbol]
        create_candlestick_macd_stochastic_chart(symbol_data, symbol, category)

# Process each category
process_data('Dividend_Kings')
process_data('Dividend_Aristocrats')
process_data('Dividend_Contenders')
