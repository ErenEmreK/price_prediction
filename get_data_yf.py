import yfinance as yf
import csv 
import pandas as pd
import os
INTERVAL = '1wk'
attributes_folder_path = 'data/yf_weekly'
recommendation_data_folder_path = 'data/recommendation_data'

def get_symbols():
    #Gets all symbols in listing status file
    df = pd.read_csv('data/listing_status.csv')
    symbols = df['symbol'].tolist()
    return symbols
    
def write_recommendation_data(recommendation_data_folder_path):
    #Writing all to seperate files is not so memory efficient
    #But it comes handy in error situations
    symbols = get_symbols()
    
    for symbol in symbols:
        recommendations = yf.Ticker(symbol).recommendations
        if recommendations.empty:
            print(f"Couldn't get recommendations for {symbol}.")
            continue
        recommendations.to_csv(f'{recommendation_data_folder_path}/{symbol}.csv', index=False)
    print("Recommendations have been written.")
   
def get_data(symbols):
    for symbol in symbols:
        hist = yf.download(symbol, period='max', interval=INTERVAL)
        if not hist.empty:
            hist.to_csv(f'{attributes_folder_path}/{symbol}.csv')
        else:
            print(f"Couldn't find data for {symbol}.") 
    print("Complete.")

def get_available_symbols():
    #Gets only the data we could wetch in our last attempt
    #So it gets rid of the data which don't give recommendations 
    folder = 'data/recommendation_data'
    files = os.listdir(folder)
    symbols = []
    for filename in files:
        if filename.endswith('.csv'):
            symbols.append(os.path.splitext(filename)[0])
    return symbols

if __name__ == '__main__':
    write_recommendation_data(recommendation_data_folder_path)



