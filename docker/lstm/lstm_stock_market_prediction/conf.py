# Model Configuration

# Local directory for the location of the compiled models
MODEL_DIR_PREFIX = "model_repo"

# Default list of ticker symbols managed by the application
TICKER_SYMBOLS = ["AMD", "AMZN", "AAPL", "GM", "GOOGL", "INTC", "MSFT", "NVDA", "PFE", "TSLA"]

# Number of lags or days the LSTM model will default to
LAGS = 60

TEST_DATA_DIR = "tests/data/historical_stock_prices"