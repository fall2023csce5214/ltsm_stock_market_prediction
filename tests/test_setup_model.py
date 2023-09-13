from typing import List

from ltsm_stock_market_prediction.ltsm import LTSMModel


def test_appl_ltsm_60_day_model(appl_60_day_closing_prices: List[float]):
    assert (len(appl_60_day_closing_prices) > 0)

    expect_closing_price = 179.34976
    ticker_symbol = "AAPL"
    lags = 60
    model = LTSMModel()

    actual_closing_price = model.predict(ticker_symbol, lags, appl_60_day_closing_prices[0])

    assert(expect_closing_price == actual_closing_price)


