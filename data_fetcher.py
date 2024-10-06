import yfinance as yf
import talib as ta  # Using TA-Lib
import matplotlib.pyplot as plt
import time

# List of Dividend Kings stock symbols
dividend_kings = ['JNJ', 'PG', 'KO', 'MMM', 'CL', 'TGT', 'MO']  # Add more symbols

# Function to fetch stock data, calculate technical indicators, and generate a chart
def fetch_data_and_generate_chart(symbol):
    # Fetch stock data for the last year
    data = yf.download(symbol, period="1y", interval="1d")
    
    # Calculate technical indicators using TA-Lib
    data['MACD'], data['MACD_signal'], data['MACD_hist'] = ta.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    data['RSI'] = ta.RSI(data['Close'], timeperiod=14)
    data['Stochastic_K'], data['Stochastic_D'] = ta.STOCH(data['High'], data['Low'], data['Close'])

    # Create subplots for Closing price, MACD, RSI, and Stochastic Oscillator
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(10, 10))
    
    # Plot closing price
    ax1.plot(data.index, data['Close'], label='Close')
    ax1.set_title(f'{symbol} Closing Price')
    ax1.legend()

    # Plot MACD
    ax2.plot(data.index, data['MACD'], label='MACD')
    ax2.plot(data.index, data['MACD_signal'], label='Signal Line')
    ax2.bar(data.index, data['MACD_hist'], label='MACD Histogram')
    ax2.set_title('MACD')
    ax2.legend()

    # Plot RSI
    ax3.plot(data.index, data['RSI'], label='RSI', color='purple')
    ax3.set_title('RSI')
    ax3.legend()

    # Plot Stochastic Oscillator
    ax4.plot(data.index, data['Stochastic_K'], label='%K', color='blue')
    ax4.plot(data.index, data['Stochastic_D'], label='%D', color='red')
    ax4.set_title('Stochastic Oscillator')
    ax4.legend()

    # Adjust layout and save the plot
    plt.tight_layout()
    plt.savefig(f'{symbol}_chart.png')
    print(f"Chart for {symbol} with technical indicators saved.\n")

# Iterate through the list of Dividend Kings, limiting requests to fewer than 5 every 2 minutes
for i, symbol in enumerate(dividend_kings):
    fetch_data_and_generate_chart(symbol)
    
    # Check if we've made 5 requests, then wait for 2 minutes
    if (i + 1) % 5 == 0:
        print("Waiting for 2 minutes to avoid API rate limits...")
        time.sleep(120)  # Wait for 2 minutes (120 seconds)
    else:
        time.sleep(30)  # Wait 30 seconds between requests
