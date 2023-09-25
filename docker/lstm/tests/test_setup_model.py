from typing import List

from lstm_stock_market_prediction.lstm import LSTMModel


def test_appl_lstm_60_day_model(appl_60_day_closing_prices: List[float]):
    assert (len(appl_60_day_closing_prices[0]) > 0)

    expect_closing_price = 179.34976
    ticker_symbol = "AAPL"
    lags = 60

    model = LSTMModel()

    # model.compile(ticker_symbol, 60)

    import ipdb; ipdb.set_trace()


    # Assert that predicted closing price is within $2
    actual_closing_price = model.predict(ticker_symbol, lags, appl_60_day_closing_prices[0])

    assert((expect_closing_price - 2) <= actual_closing_price <= (expect_closing_price + 2))


