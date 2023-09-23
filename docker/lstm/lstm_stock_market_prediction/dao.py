from datetime import datetime
import logging
import os
import pandas as pd
from pandas import DataFrame
from sqlalchemy import create_engine
from sqlalchemy import text
import yfinance as yf

from lstm_stock_market_prediction.conf import TICKER_SYMBOLS


logger = logging.getLogger(__name__)
DB_ERROR_MESSAGE = "Unable to connect to the stocks database."
DB_CONNECTION_STRING = f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}/{os.environ['DB_NAME']}"


def run():
    try:
        stocks = extract()
        load(stocks)
    except Exception as e:
        logger.warning("Unable to connect to the stocks database.", exc_info=True)
        raise e


def extract(ticker_symbols=TICKER_SYMBOLS,
            start='2012-01-01',
            end=datetime.now()) -> DataFrame:
    stocks = pd.concat([yf.download(ticker,
                                    group_by="Ticker",
                                    start=start,
                                    end=end).assign(ticker=ticker) for ticker in ticker_symbols],
                       ignore_index=False)

    stocks['trading_date'] = stocks.index

    stocks.rename(columns={"Open": "open_price",
                           "High": "high_price",
                           "Low": "low_price",
                           "Close": "close_price",
                           "Adj Close": "adj_close_price",
                           "Volume": "volume"},
                           inplace=True)

    return stocks


def load(df: DataFrame) -> None:
    engine = create_engine(DB_CONNECTION_STRING)

    with engine.begin() as conn:
        logger.debug("We are connected to the stocks database.")

        conn.execute(text("delete from stock_analysis.stock"))

        logger.debug("Refreshed database.")

        df.to_sql("stock",
                  schema="stock_analysis",
                  con=conn,
                  if_exists='append',
                  index=False)


if __name__ == "__main__":
    run()
