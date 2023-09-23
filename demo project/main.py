from fastapi import FastAPI, HTTPException, Query
from datetime import datetime
from model import fetch_stock_data, train_linear_regression_model
import uvicorn
import socket
import os

app = FastAPI()

# Load historical data and train the model
data = fetch_stock_data('AAPL', '2020-01-01', '2021-12-31')
X = data.index.values.reshape(-1, 1)
y = data['Close']
model, rmse = train_linear_regression_model(X, y)

@app.get("/")
async def read_root(date: str = Query(..., description="Date in YYYY-MM-DD format")):
    try:
        date = datetime.strptime(date, '%Y-%m-%d')
        prediction = model.predict([[date.toordinal()]])
        return {"date": date.strftime('%Y-%m-%d'), "predicted_price": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == '__main__':
    uvicorn.run(app, host=socket.gethostname(), port=int(os.environ["PORT"]))
