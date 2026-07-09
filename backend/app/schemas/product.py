from pydantic import BaseModel


class ProductCreate(BaseModel):
    title: str
    url: str
    store: str
    image: str = ""
    current_price: float
    rating: float = 0
    reviews: int = 0


class ProductResponse(BaseModel):
    id: int
    title: str
    url: str
    store: str
    image: str
    current_price: float
    rating: float
    reviews: int

    class Config:
        from_attributes = True