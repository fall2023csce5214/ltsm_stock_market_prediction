from datetime import datetime
from joblib import dump, load
from keras.models import Sequential
from keras.layers import Dense, LSTM
import numpy as np
import os
import pandas as pd
from pandas_datareader import data as pdr
import scipy
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras import Sequential
import sys
import yfinance as yf


from ltsm_stock_market_prediction.conf import CONF

COMPANY_NAME = ["APPLE", "GOOGLE", "MICROSOFT", "AMAZON"]

# The tech stocks we'll use for this analysis
TICKER_SYMBOLS = ['AAPL', 'GOOG', 'MSFT', 'AMZN']


def load_model(ticker_symbol: str, lags: int) -> Sequential:
    model_pkl_file_name = CONF[ticker_symbol]["models"][str(lags)]

    # TODO - Come back to a better way to pull off the path more cleanly
    model_pkl_file = os.path.join(os.path.dirname(__file__),
                                  f"model_repo/{model_pkl_file_name}")

    model = load(model_pkl_file)

    return model


def compile_model(ticker_symbol: str, lags: int, start='2012-01-01', end=datetime.now()) -> None:
    # For reading stock data from yahoo
    yf.pdr_override()

    # Get the stock quote
    df = pdr.get_data_yahoo(ticker_symbol, start=start, end=end)

    # Create a new dataframe with only the 'Close column
    data = df.filter(['Close'])
    # Convert the dataframe to a numpy array
    dataset = data.values

    # Get the number of rows to train the model on
    training_data_len = int(np.ceil(len(dataset) * .95))

    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(dataset)

    # Create the training data set
    # Create the scaled training data set
    train_data = scaled_data[0:int(training_data_len), :]
    # Split the data into x_train and y_train data sets
    x_train = []
    y_train = []

    for i in range(60, len(train_data)):
        x_train.append(train_data[i - 60:i, 0])
        y_train.append(train_data[i, 0])

    # Convert the x_train and y_train to numpy arrays
    x_train, y_train = np.array(x_train), np.array(y_train)

    # Reshape the data
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    # Build the LSTM model
    model = Sequential()
    model.add(LSTM(128, return_sequences=True, input_shape=(x_train.shape[1], 1)))
    model.add(LSTM(64, return_sequences=False))
    model.add(Dense(25))
    model.add(Dense(1))

    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train the model
    model.fit(x_train, y_train, batch_size=1, epochs=1)

    # Save model to disk
    # save the LTSM RNN model as a pickle file
    model_pkl_file_name = CONF[ticker_symbol]["models"][str(lags)]

    model_pkl_file = os.path.join(os.path.dirname(__file__),
                                  f"model_repo/{model_pkl_file_name}")

    # with open(model_pkl_file, 'wb') as file:
    # dump(model, file)
    dump(model, model_pkl_file)





