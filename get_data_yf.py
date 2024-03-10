import yfinance as yf
import csv 
#msft.recommendations can be useful
INTERVAL = '1wk'
folder_path = 'data/yf_weekly'

def get_symbols():
    #TODO get all available symbols from yahoo/ listing_status.csv
    #TODO save symbols to reduce api usage
    
    
    #we return small set for now
    symbols = ['AAPL', 'MSFT', 'XWEL', 'YJ', 'YHGJ', 'ZEUS', 'XTLB', 'IBM',
               'NFLX', 'V', 'CRM', 'DIS', 'TSLA', 'BA', 'AMZN', 'CRM', 'FB',
               'INTC', 'BABA', 'HD', 'PYPL', 'NKE', 'XOM', 'CSCO', 'MRK', 'UNH']
    return symbols

def get_data(symbols):
    for symbol in symbols:
        hist = yf.download(symbol, period='max', interval=INTERVAL)
        if not hist.empty:
            hist.to_csv(f'{folder_path}/{symbol}.csv')
        else:
            print(f"Couldn't find data for {symbol}.") 
    print("Complete.")

def main():
    symbols = get_symbols()
    get_data(symbols)
    
if __name__ == '__main__':
    main()




