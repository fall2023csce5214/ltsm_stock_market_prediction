import argparse
import os
from datetime import datetime
import logging
import multiprocessing
from multiprocessing import Pool
import pandas as pd
from pandas import DataFrame
from typing import List, Tuple
import yfinance as yf

from lstm_stock_market_prediction.conf import LAGS, TEST_DATA_DIR, TICKER_SYMBOLS
from lstm_stock_market_prediction.dao import StockDAO
from lstm_stock_market_prediction.lstm import LSTMModel
from lstm_stock_market_prediction.model import convert_date, DATE_FORMAT

logger = logging.getLogger(__name__)
DB_ERROR_MESSAGE = "Unable to connect to the stocks database."
NUMBER_OF_CPUS = multiprocessing.cpu_count()


def run(ticker_symbols: List[str],
        start_date: datetime,
        end_date: datetime,
        lags: int,
        load_data: bool,
        compile_models: bool,
        remote_data: bool) -> None:

    try:
        if load_data:
            logger.warning("Extracting historical stock dataset")
            stocks = extract(ticker_symbols, start_date, end_date, remote_data)

            logger.warning("Loading historical stock dataset")
            load(stocks)

        if compile_models:
            logger.warning("Compiling LSTM models")

            parallel_ticker_symbols = []

            for ticker_symbol in ticker_symbols:
                parallel_ticker_symbols.append((ticker_symbol, start_date, end_date, lags))

            pool = Pool(processes=NUMBER_OF_CPUS)
            pool.map(parallel_compile, parallel_ticker_symbols)

    except Exception as e:
        logger.warning("Unable to connect to the stocks database.", exc_info=True)
        raise e


def extract(ticker_symbols: List[str],
            start: str,
            end: str,
            remote_data) -> DataFrame:

    if remote_data:
        stocks = pd.concat([yf.download(ticker,
                                        group_by="Ticker",
                                        start=start,
                                        end=end).assign(ticker=ticker) for ticker in ticker_symbols],
                           ignore_index=False)
        transform(stocks)
    else:
        stocks = DataFrame()
        stock_files = os.listdir(TEST_DATA_DIR)

        for stock_file in stock_files:
            ticker_symbol_stock = pd.read_csv(os.path.join(TEST_DATA_DIR, stock_file))
            ticker_symbol = stock_file.split(".")[0]
            ticker_symbol_stock["ticker"] = ticker_symbol
            stocks = pd.concat([stocks, ticker_symbol_stock])

        transform(stocks)

    return stocks


def transform(stocks: DataFrame) -> None:
    if "Date" not in stocks.columns:
        stocks['trading_date'] = stocks.index

    stocks.rename(columns={"Open": "open_price",
                           "High": "high_price",
                           "Low": "low_price",
                           "Close": "close_price",
                           "Adj Close": "adj_close_price",
                           "Volume": "volume",
                           "Date": "trading_date"},
                  inplace=True)


def load(df: DataFrame) -> None:
    StockDAO.load_stocks(df)


def parallel_compile(param: Tuple[str, str, str]) -> None:
    ticker_symbol = param[0]
    start = param[1]
    end = param[2]
    lags = param[3]

    model = LSTMModel()

    logger.warning(f"Compiling {ticker_symbol} LSTM Model for {lags} day lag.")
    model.compile(ticker_symbol, lags, start, end)


def compile(ticker_symbols: List[str], lags: int, start: str, end: str) -> None:

    model = LSTMModel()

    for ticker_symbol in ticker_symbols:
        logger.warning(f"Compiling {ticker_symbol} LSTM Model for {lags} day lag.")
        model.compile(ticker_symbol, lags, start, end)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--ticker_symbols', action='append')
    parser.add_argument('-l', '--lags', type=int, default=LAGS)
    parser.add_argument('-s',
                        '--start_date',
                        type=lambda date: datetime.strptime(date, DATE_FORMAT),
                        default='2012-01-01')
    parser.add_argument('-e', '--end_date', type=datetime, default=datetime.now())
    parser.add_argument('-d', '--load_data', action='store_true', default=False)
    parser.add_argument('-c', '--compile_models', action='store_true', default=False)
    parser.add_argument('-r', '--remote_data', action='store_true', default=False)
    args = parser.parse_args()

    ticker_symbols = args.ticker_symbols

    if not ticker_symbols:
        ticker_symbols = TICKER_SYMBOLS

    start_date = convert_date(args.start_date)
    end_date = convert_date(args.end_date)
    lags = args.lags
    compile_models = args.compile_models
    load_data = args.load_data
    remote_data = args.remote_data

    run(ticker_symbols, start_date, end_date, lags, load_data, compile_models, remote_data)
