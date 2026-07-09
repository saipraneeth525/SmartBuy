from pydantic import BaseModel


class RecommendationResponse(BaseModel):
    product: str
    current_price: float
    minimum_price: float
    maximum_price: float
    average_price: float
    recommendation: str
    confidence: int
    reason: str
    target_price: float