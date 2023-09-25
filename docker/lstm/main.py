from datetime import date, timedelta
from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from typing import Union


from lstm_stock_market_prediction.dao import StockDAO
from lstm_stock_market_prediction.conf import LAGS
from lstm_stock_market_prediction.lstm import LSTMModel
from lstm_stock_market_prediction.model import convert_date, StockMarketPrediction

app = FastAPI()


@app.get("/predict", response_model=StockMarketPrediction)
async def predict(ticker_symbol: str,
                  date: date,
                  model=Depends(LSTMModel)) -> Union[StockMarketPrediction, JSONResponse]:
    try:
        start_date = convert_date(date - timedelta(days=LAGS - 1))
        end_date = convert_date(date)
        closing_prices = StockDAO.get_closing_prices(ticker_symbol, start_date, end_date).to_numpy()

        if closing_prices.any():
            closing_price = model.predict(ticker_symbol, LAGS, closing_prices)
            prediction = StockMarketPrediction(trading_date=date, closing_price=closing_price)

            return prediction
        else:
            return JSONResponse(content={"message": f"There are not enough {LAGS} day closing prices for symbol {ticker_symbol} between {start_date} and {end_date}"})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))