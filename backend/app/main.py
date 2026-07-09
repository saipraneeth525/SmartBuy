from fastapi import FastAPI
from app.api.v1.users import router as users_router
from app.api.v1.auth import router as auth_router
from app.api.v1.products import router as products_router
from app.api.v1.price_history import router as price_history_router

app = FastAPI(
    title="SmartBuy API",
    version="1.0.0",
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(products_router)
app.include_router(price_history_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to SmartBuy Backend 🚀"
    }