#!/bin/sh

# Uncomment this line to compile the models before startup
# Seed the data
# poetry run python -m lstm_stock_market_prediction.etl -d -c

# Comment out the following line for trouble-shooting locally
poetry run python -m uvicorn main:app --reload --port=$WEB_SERVICE_PORT --host=0.0.0.0

# Uncomment the following lines for trouble-shooting locally
# touch /tmp/lstm.log
# tail -f /tmp/lstm.log