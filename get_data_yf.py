import yfinance as yf
import csv 
import pandas as pd
INTERVAL = '1wk'
attributes_folder_path = 'data/yf_weekly'
recommendation_data_folder_path = 'data/recommendation_data'

def get_symbols():
    #TODO get all available symbols from yahoo/ listing_status.csv
    #TODO save symbols to reduce api usage
    #TODO get only listed symbols
    
    df = pd.read_csv('data/listing_status.csv')
    symbols = df[['symbol']].items()
    print(symbols)
    
    #TODO GET ALL

def get_symbols_sample():
    
    #we return small set for now
    symbols = ['AAPL', 'MSFT', 'XWEL', 'YJ', 'YHGJ', 'ZEUS', 'XTLB', 'IBM',
               'NFLX', 'V', 'CRM', 'DIS', 'TSLA', 'BA', 'AMZN', 'CRM', 'FB',
               'INTC', 'BABA', 'HD', 'PYPL', 'NKE', 'XOM', 'CSCO', 'MRK', 'UNH']

    return symbols
    
def write_recommendation_data(recommendation_data_folder_path):
    symbols = get_symbols_sample()
    for symbol in symbols:
        recommendations = yf.Ticker(symbol).recommendations
        if recommendations.empty:
            print(f"Couldn't get recommendations for {symbol}.")
            continue
        recommendations.to_csv(f'{recommendation_data_folder_path}/{symbol}_rec.csv', index=False)
    print("Recommendations have been written.")

def get_data(symbols):
    for symbol in symbols:
        hist = yf.download(symbol, period='max', interval=INTERVAL)
        if not hist.empty:
            hist.to_csv(f'{attributes_folder_path}/{symbol}.csv')
        else:
            print(f"Couldn't find data for {symbol}.") 
    print("Complete.")

def main():
    symbols = get_symbols()
    get_data(symbols)
    
if __name__ == '__main__':
    #main()
    pass




