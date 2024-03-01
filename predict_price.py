import pandas as pd


def listing_status_request():
    #This fn will get current listing status csv file
    #We dont need right now
    import requests

    path = 'data\listing_status.csv'
    
    #Can replace "demo" with or API key, though not necessary
    url = 'https://www.alphavantage.co/query?function=LISTING_STATUS&apikey={}'
    response = requests.get(url.format("demo"))
      
    if response.status_code == 200:
        with open(path, 'wb') as f:
            f.write(response.content)
        print("Listing Status CSV file saved successfully.")
    else:
        print("Failed to fetch data from the URL.")
        
def get_symbols():
    #TODO data arranging, return listed and delisted company symbols as lists
    #df = pd.read_csv('data\listing_status.csv')
       
    #we are gonna return small sample for now

    listed = ['AAPL', 'AAPU', 'AAPX', 'AAPY', 'AAT', 'AAU', 'AAXJ', 'AB', 'ABAT', 'ABBV', 'ABCB', 'ABCL', 'ABCS', 'ABEO', 'ABEQ', 'ABEV', 'ABG', 'ABIO', 'ABL', 'ABLLL', 'ABLLW']
    delisted = ['TINY', 'TIOA', 'TIOAU', 'TIOAW', 'TIPD', 'TIPL', 'TIS', 'TISA', 'TIVO', 'TKF', 'TKKSR', 'TKKSU', 'TKMR', 'TKPPY', 'TLC', 'TLCVF', 'TLDH']

    return listed, delisted

def get_data(symbols):
    for symbol in symbols:
        url = f''




def main():
    l_symbols, d_symbols = get_symbols()
    

