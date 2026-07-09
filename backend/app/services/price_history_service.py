from sqlalchemy.orm import Session

from app.models.price_history import PriceHistory


def add_price(
    db: Session,
    product_id: int,
    price: float,
):
    history = PriceHistory(
        product_id=product_id,
        price=price,
    )

    db.add(history)
    db.commit()
    db.refresh(history)

    return history


def get_price_history(
    db: Session,
    product_id: int,
):
    return (
        db.query(PriceHistory)
        .filter(
            PriceHistory.product_id == product_id
        )
        .order_by(
            PriceHistory.checked_at.desc()
        )
        .all()
    )