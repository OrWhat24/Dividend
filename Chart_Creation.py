import os

# Example directory structure
chart_output_dirs = {
    'Dividend_Kings': "Charts/Dividend_Kings",
    'Dividend_Aristocrats': "Charts/Dividend_Aristocrats",
    'Dividend_Contenders': "Charts/Dividend_Contenders"
}

analysis_output_dirs = {
    'Dividend_Kings': "Analysis/Dividend_Kings",
    'Dividend_Aristocrats': "Analysis/Dividend_Aristocrats",
    'Dividend_Contenders': "Analysis/Dividend_Contenders"
}

# Ensure directories exist
for folder in chart_output_dirs.values():
    if not os.path.exists(folder):
        os.makedirs(folder)

for folder in analysis_output_dirs.values():
    if not os.path.exists(folder):
        os.makedirs(folder)

# Function to create a text file for analysis
def create_analysis_file(symbol, category):
    analysis_path = os.path.join(analysis_output_dirs[category], f"{symbol}_analysis.txt")
    with open(analysis_path, 'w') as f:
        f.write(f"Analysis for {symbol}\n")
        f.write("Insert your commentary and technical analysis here...\n")
    print(f"Created analysis file for {symbol} at {analysis_path}")

# Modify chart creation to also generate analysis file
def create_candlestick_chart_with_analysis(data, symbol, category):
    # Your existing chart creation code here...
    
    # Create a corresponding analysis file
    create_analysis_file(symbol, category)

# Example of generating chart and analysis for a stock
# process_data function would call create_candlestick_chart_with_analysis
