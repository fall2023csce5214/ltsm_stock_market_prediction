from typing import List
from ltsm_stock_market_prediction.algo import load_algo


def test_appl_ltsm_60_day_model(appl_60_day_closing_prices: List[float]):
    assert (len(appl_60_day_closing_prices) > 0)

    expect_closing_price = 151.91999817

    model = load_algo(ticker_symbol="APPL", lags=60)

    actual_closing_price = ...
