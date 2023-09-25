from joblib import dump, load
from keras.models import Sequential
from keras.layers import Dense, LSTM
import numpy as np
import os
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras import Sequential

from lstm_stock_market_prediction.conf import MODEL_DIR_PREFIX
from lstm_stock_market_prediction.dao import StockDAO


class LSTMModel:
    SCALER = MinMaxScaler(feature_range=(0, 1))

    @staticmethod
    def load(ticker_symbol: str, lags: int) -> Sequential:
        model_pkl_file = LSTMModel.get_pkl_file_name(ticker_symbol, lags)
        model = load(model_pkl_file)

        return model

    @staticmethod
    def compile(ticker_symbol: str,
                lags: int,
                start: str,
                end: str,
                epochs=1,
                batch_size=1) -> None:
        # Get the stock quote
        df = StockDAO.get_closing_prices(ticker_symbol, start, end)

        # Create a new dataframe with only the 'Close column
        data = df.filter(['close_price'])
        # Convert the dataframe to a numpy array
        dataset = data.values

        # Get the number of rows to train the model on
        training_data_len = int(np.ceil(len(dataset) * .95))

        scaled_data = LSTMModel.SCALER.fit_transform(dataset)

        # Create the training data set
        # Create the scaled training data set
        train_data = scaled_data[0:int(training_data_len), :]
        # Split the data into x_train and y_train data sets
        x_train = []
        y_train = []

        for i in range(lags, len(train_data)):
            x_train.append(train_data[i - lags:i, 0])
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
        model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs)

        # Save model to disk
        # save the LTSM RNN model as a pickle file
        model_pkl_file = LSTMModel.get_pkl_file_name(ticker_symbol, lags)

        dump(model, model_pkl_file)

    @staticmethod
    def predict(ticker_symbol: str, lags: int, closing_prices: np.ndarray) -> float:
        closing_prices_scaled = LSTMModel.SCALER.fit_transform(closing_prices)

        model = LSTMModel.load(ticker_symbol=ticker_symbol, lags=lags)

        prediction = model.predict(closing_prices_scaled)
        prediction = LSTMModel.SCALER.inverse_transform(prediction)

        return round(prediction[-1:][0][0], 2)

    @staticmethod
    def get_pkl_file_name(ticker_symbol: str, lags: int):
        return os.path.join(os.path.dirname(__file__),
                            f"{MODEL_DIR_PREFIX}/{ticker_symbol}_ltsm_{lags}_day_model.pkl")







