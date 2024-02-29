import pandas as pd

def get_symbols():
    #May have usage limit
    #We return sample for now 
    
    """
    API_KEY = 'OQMQKBKE8VKUOZ2U'
    
    #This gets all listed nasdaq symbols
    CSV_URL = "https://www.alphavantage.co/query?function=LISTING_STATUS&state={}&apikey={}"
    
    listed = pd.read_csv(CSV_URL.format('listed', API_KEY))
    listed_symbols = listed['symbol'].tolist()
    
    
    delisted = pd.read_csv(CSV_URL.format('delisted', API_KEY))
    delisted_symbols = delisted['symbol'].tolist()
    
    print(listed_symbols)
    """

    listed = ['AAPL', 'AAPU', 'AAPX', 'AAPY', 'AAT', 'AAU', 'AAXJ', 'AB', 'ABAT', 'ABBV', 'ABCB', 'ABCL', 'ABCS', 'ABEO', 'ABEQ', 'ABEV', 'ABG', 'ABIO', 'ABL', 'ABLLL', 'ABLLW']
    delisted = ['TINY', 'TIOA', 'TIOAU', 'TIOAW', 'TIPD', 'TIPL', 'TIS', 'TISA', 'TIVO', 'TKF', 'TKKSR', 'TKKSU', 'TKMR', 'TKPPY', 'TLC', 'TLCVF', 'TLDH']

    return listed, delisted
 
get_symbols()