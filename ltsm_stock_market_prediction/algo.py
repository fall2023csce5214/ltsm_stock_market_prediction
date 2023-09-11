import os
import pickle
from ltsm_stock_market_prediction.conf import CONF


def load_algo(ticker_symbol: str, lags: int):
    pickled_model_file_name = CONF[ticker_symbol]["models"][str(lags)]

    # TODO - Come back to a better way to pull off the path more cleanly
    pickled_model_file_path = os.path.join(os.path.dirname(__file__),
                                           f"../ltsm_stock_market_prediction/model_repo/{pickled_model_file_name}")

    with open(pickled_model_file_path, 'rb') as pickled_model_file:
        model = pickle.load(pickled_model_file)

    return model
