from datetime import date, datetime
from pydantic import BaseModel, validator

DATE_FORMAT = '%Y-%m-%d'


def convert_date(date: datetime) -> str:
    return date.strftime(DATE_FORMAT)


class StockMarketPrediction(BaseModel):
    trading_date: date
    closing_price: float

    class Config:
        json_encoders = {
            datetime:  convert_date
        }

    @validator('closing_price')
    def result_check(cls, v):
        ...
        return round(v, 2)
