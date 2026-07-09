from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.db.dependencies import get_db
from app.models.user import User
from app.services.product_service import get_product
from app.services.price_history_service import (
    add_price,
    get_price_history,
)
from app.schemas.price_history import (
    PriceHistoryCreate,
    PriceHistoryResponse,
)

router = APIRouter(
    prefix="/products",
    tags=["Price History"],
)


@router.post(
    "/{product_id}/price",
    response_model=PriceHistoryResponse,
)
def add_product_price(
    product_id: int,
    payload: PriceHistoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    product = get_product(
        db,
        product_id,
        current_user.id,
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return add_price(
        db,
        product_id,
        payload.price,
    )


@router.get(
    "/{product_id}/history",
    response_model=list[PriceHistoryResponse],
)
def product_history(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    product = get_product(
        db,
        product_id,
        current_user.id,
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return get_price_history(
        db,
        product_id,
    )