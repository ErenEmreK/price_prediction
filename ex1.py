import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense

from datetime import datetime

# Step 1: Load the Data
df = pd.read_csv('data/yf_attributes/AAPL.csv')  # Replace 'company_data.csv' with your file path
def date_to_int(str_date):
    #converts 'YYYY-MM-DD' to integer
    time_obj = datetime.strptime(str_date, r'%Y-%m-%d')
    ordinal = time_obj.toordinal()
    return ordinal

df['Date'] = [date_to_int(date) for date in df['Date']]

# Step 2: Preprocess the Data
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df)

# Define function to create sequences
def create_sequences(data, seq_length):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i+seq_length])
        y.append(data[i+seq_length, 4])  # Using 'Close' price as the target
    return np.array(X), np.array(y)

# Define sequence length
seq_length = 12  # Choose an appropriate sequence length

# Create sequences
X, y = create_sequences(scaled_data, seq_length)

# Step 3: Split the Data
split_ratio = 0.8  # 80% training data, 20% testing data
split_index = int(split_ratio * len(X))

X_train, X_test = X[:split_index], X[split_index:]
y_train, y_test = y[:split_index], y[split_index:]

# Step 4: Define the LSTM Model
model = Sequential([
    LSTM(50, input_shape=(X_train.shape[1], X_train.shape[2])),
    Dense(1)
])

# Step 5: Compile the Model
model.compile(optimizer='adam', loss='mean_squared_error')

# Step 6: Train the Model
model.fit(X_train, y_train, epochs=50, batch_size=32, verbose=1)

# Step 7: Evaluate the Model
loss = model.evaluate(X_test, y_test)
print("Test Loss:", loss)

# Step 8: Make Predictions
predictions = model.predict(X_test)
