from datetime import datetime

from pydantic import BaseModel


class PriceHistoryCreate(BaseModel):
    price: float


class PriceHistoryResponse(BaseModel):
    id: int
    price: float
    checked_at: datetime

    class Config:
        from_attributes = True