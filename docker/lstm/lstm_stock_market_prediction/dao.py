import logging
import os
from pandas import DataFrame
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text


logger = logging.getLogger(__name__)
DB_CONNECTION_STRING = f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}/{os.environ['DB_NAME']}"


class StockDAO:
    @staticmethod
    def load_stocks(df: DataFrame):
        engine = StockDAO.get_engine()

        with engine.begin() as conn:
            logger.debug("We are connected to the stocks database.")

            conn.execute(text("delete from stock_analysis.stock"))

            logger.debug("Refreshed database.")

            df.to_sql("stock",
                      schema="stock_analysis",
                      con=conn,
                      if_exists='append',
                      index=False)

    @staticmethod
    def get_closing_prices(ticker_symbol: str,
                           start_date: str,
                           end_date: str) -> DataFrame:
        engine = StockDAO.get_engine()

        sql = text("""
            select close_price 
            from stock_analysis.stock 
            where trading_date >= :start_date and trading_date <= :end_date and ticker = :ticker
        """)

        params = {"ticker": ticker_symbol,
                  "start_date": start_date,
                  "end_date": end_date}

        with engine.begin() as conn:
            return pd.read_sql_query(sql=sql, params=params, con=conn)

    @staticmethod
    def get_engine():
        return create_engine(DB_CONNECTION_STRING)
