from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout, Normalization
import os
import pandas as pd
import numpy as np
from predict import date_to_int
from sklearn.preprocessing import MinMaxScaler, StandardScaler

TRAIN_RATIO = 0.8
TIMESTEP = 30

def create_model(input_shape):
    
    model = Sequential()
    model.add(LSTM(units=50, input_shape=input_shape, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50,return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50,return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50,return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50,return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50,return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))
    model.compile(optimizer='adam',loss='mean_squared_error')
        
    return model

df = pd.read_csv('data/yf_attributes/AAPL.csv')
df['Date'] = [date_to_int(date) for date in df['Date']]

X_sc = MinMaxScaler()
scaled_X = X_sc.fit_transform(df)

targets = df[['Close']]
y_sc = MinMaxScaler()
scaled_y = y_sc.fit_transform(targets)

def create_sequences(scaled_X, scaled_y, timestep):
    X, y = [], []
    for i in range(len(scaled_X) - timestep):
        X.append(scaled_X[i:i + timestep]) #Using all data between timesteps
        y.append(scaled_y[i + timestep]) #Using next timesteps close data as target
    
    return np.array(X), np.array(y)


X, y = create_sequences(scaled_X, scaled_y, TIMESTEP)

split_point = int(TRAIN_RATIO * len(X))
X_train, y_train = X[:split_point], y[:split_point]
X_test, y_test = X[split_point:], y[split_point:]


model = create_model((X_train.shape[1], X_train.shape[2]))
model.fit(X_train, y_train, epochs=20, batch_size=32)


loss = model.evaluate(X_test, y_test)
print("Test Loss:", loss)


last_sequence = X_test[-1].reshape(1, X_test[-1].shape[0], X_test[-1].shape[1])

scaled_prediction = model.predict(last_sequence)

prediction = y_sc.inverse_transform(scaled_prediction)

last_y = y_sc.inverse_transform([y_test[-1]])
print(last_y, prediction)

test_predictions = model.predict(X_test)
test_predictions = y_sc.inverse_transform(test_predictions)

train_predictions = model.predict(X_train)
train_predictions = y_sc.inverse_transform(train_predictions)

train_target_values = y_sc.inverse_transform(y_train)
test_target_values = y_sc.inverse_transform(y_test)


