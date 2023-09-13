from ltsm_stock_market_prediction.algo import load_model
from sklearn.preprocessing import MinMaxScaler
from typing import List


def test_appl_ltsm_60_day_model(appl_60_day_closing_prices: List[float]):
    assert (len(appl_60_day_closing_prices) > 0)

    expect_closing_price = 179.34976

    scaler = MinMaxScaler(feature_range=(0, 1))
    expect_closing_prices_scaled = scaler.fit_transform(appl_60_day_closing_prices[0])

    model = load_model(ticker_symbol="AAPL", lags=60)

    prediction = model.predict(expect_closing_prices_scaled)
    prediction = scaler.inverse_transform(prediction)

    actual_closing_price = prediction[-1:]

    assert(expect_closing_price == actual_closing_price)


