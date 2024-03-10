#This file ultimately will get all relevant attributes for possible companies
#And will write into a csv file

import pandas as pd
import requests
import csv

API_KEY = 'ALPHAVANTAGE_API_KEY'
FREQUENCY = 'MONTHLY' #we can set this to 'DAILY' or 'WEEKLY'

def listing_status_request():
    #This fn will get current listing status csv file
    #We dont need right now
    path = 'data/av_listing_status.csv'
    
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

    listed = ['AAPL', 'AAPU', 'GOOGL', 'MSFT', 'ABAT', 'ABBV', 'ABCB', 'ABCL', 'ABCS', 'ABEO', 'ABEQ', 'ABEV', 'ABG', 'ABIO', 'ABL', 'ABLLL', 'ABLLW']
    delisted = ['TINY', 'TIOA', 'TIOAU', 'TIOAW', 'TIPD', 'TIPL', 'TIS', 'TISA', 'TIVO', 'TKF', 'TKKSR', 'TKKSU', 'TKMR', 'TKPPY', 'TLC', 'TLCVF', 'TLDH']

    #we test listed ones for now
    return delisted

def get_data_files(symbols):
    fieldnames = ['date', 'open', 'high', 'low', 'close', 'volume']     
    
    for symbol in symbols:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_{FREQUENCY}&symbol={symbol}&apikey={API_KEY}'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            time_series = data.get('Monthly Time Series')
            
            if time_series:
                with open(f'data/av_attributes/{symbol}.csv', 'w', newline='') as csvfile:  
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    
                    for date, values in time_series.items():
                        writer.writerow({
                            'date': date,
                            'open': values['1. open'],
                            'high': values['2. high'],
                            'low': values['3. low'],
                            'close': values['4. close'],
                            'volume': values['5. volume']
                        })
            else:
                print(f"Couldn't get the time series data for {symbol}.")
        else: 
            print(f"Couldn't fetch the data for {symbol}.")        
            
    return 

def main():
    #ALPHA VANTAGE has very low usage limit for free-tier 
    #so we won't get data for every symbol
    #TODO migrate to Yahoo Finance API instead
    symbols = get_symbols()
    get_data_files(symbols)

main()


