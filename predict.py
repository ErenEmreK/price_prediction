import os
import pandas as pd
from datetime import datetime
import numpy as np

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
            
def train_test_split(X, y, train_ratio):
    split_point = int(train_ratio * len(X))
    X_train, y_train = X[:split_point], y[:split_point]
    X_test, y_test = X[split_point:], y[split_point:]

    return X_train, y_train, X_test, y_test

def preprocess(df):
    #convert dates to integer, then rescales them between 0 and 1
    df['Date'] = [date_to_int(date) for date in df['Date']]
    
    return 

def create_sequences(scaled_X, scaled_y, timestep):
    X, y = [], []
    for i in range(len(scaled_X) - timestep):
        X.append(scaled_X[i:i + timestep]) #Using all data between timesteps
        y.append(scaled_y[i + timestep]) #Using next timesteps close data as target
    
    return np.array(X), np.array(y)