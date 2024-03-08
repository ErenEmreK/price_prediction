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

def advisable(test_predictions, test_targets):
    #very primitive function to assess advices on ups and downs
    correct_ups = 0
    wrong_ups = 0
    correct_downs = 0
    wrong_downs = 0
    
    for i in range(1, len(test_predictions)):
        if test_predictions[i] > test_predictions[i-1]:
            if test_targets[i] > test_targets[i-1]:
                correct_ups += 1 
            else: 
                wrong_ups += 1
        else:
            if test_targets[i] > test_predictions[i-1]:
                wrong_downs += 1
            else:
                correct_downs += 1
    #returns (efficiency regarding ups, efficiency regarding downs)
    return correct_ups / (correct_ups + wrong_ups), correct_downs / (correct_downs + wrong_downs)