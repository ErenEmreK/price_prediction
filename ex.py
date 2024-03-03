"""
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
"""
import os
import pandas as pd
import numpy as np
from datetime import datetime
#from predict import preprocess, train_test_split, df_yielder
from sklearn.preprocessing import MinMaxScaler

TEST_RATIO = 0.2
TIMESTEPS = 12

df = pd.read_csv('data/yf_attributes/AAPL.csv')

def date_to_int(str_date):
    #converts 'YYYY-MM-DD' to integer
    time_obj = datetime.strptime(str_date, r'%Y-%m-%d')
    ordinal = time_obj.toordinal()
    return ordinal

df['Date'] = [date_to_int(date) for date in df['Date']]

scaler = MinMaxScaler()
scaled_df = scaler.fit_transform(df)

print(scaled_df)