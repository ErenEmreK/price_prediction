import tensorflow as tf
from tensorflow import keras
import os
import pandas as pd
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler

def date_to_int(str_date):
    #converts 'YYYY-MM-DD' to integer
    time_obj = datetime.strptime(str_date, r'%Y-%m-%d')
    ordinal = time_obj.toordinal()
    return ordinal

def df_yielder(folder):
    #we use yield method for memory efficiency
    for file_name in os.listdir(folder):
        if file_name.endswith('.csv'):
            file_path = os.path.join(folder, file_name)
            df = pd.read_csv(file_path)
            
            yield df
            
def train_test_split(X, y, test_ratio):
    #we are going to save last %20 as test data
    #TODO experiment with reverse splitting
    split_point = int((1 - test_ratio) * len(y))
    
    X_train, y_train = X.iloc[:split_point], y.iloc[:split_point]
    X_test, y_test = X.iloc[split_point:], y.iloc[split_point:]
    
    return X_train, y_train, X_test, y_test

def preprocess(df):
    #convert dates to integer, then rescales them between 0 and 1
    df['Date'] = [date_to_int(date) for date in df['Date']]
    
    return 
