from sqlalchemy.orm import Session

from app.models.product import Product
from app.models.price_history import PriceHistory


def analyze_product(
    db: Session,
    product_id: int,
):
    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if product is None:
        return None

    history = (
        db.query(PriceHistory)
        .filter(
            PriceHistory.product_id == product_id
        )
        .order_by(PriceHistory.checked_at.asc())
        .all()
    )

    if not history:
        return {
            "product": product.title,
            "current_price": product.current_price,
            "minimum_price": product.current_price,
            "maximum_price": product.current_price,
            "average_price": product.current_price,
            "recommendation": "NOT ENOUGH DATA",
            "confidence": 0,
            "reason": "No historical prices available.",
            "target_price": product.current_price,
        }

    prices = [p.price for p in history]

    current = prices[-1]
    minimum = min(prices)
    maximum = max(prices)
    average = sum(prices) / len(prices)

    trend = "STABLE"

    if len(prices) >= 2:
        if prices[-1] < prices[-2]:
            trend = "DOWN"
        elif prices[-1] > prices[-2]:
            trend = "UP"

    if current <= minimum:
        recommendation = "BUY NOW"
        confidence = 95
        reason = "Lowest price recorded."

    elif trend == "DOWN":
        recommendation = "GOOD DEAL"
        confidence = 88
        reason = "Price is decreasing."

    elif trend == "UP":
        recommendation = "WAIT"
        confidence = 82
        reason = "Price is increasing."

    elif current < average:
        recommendation = "GOOD DEAL"
        confidence = 75
        reason = "Current price is below average."

    else:
        recommendation = "WAIT"
        confidence = 70
        reason = "Current price is above average."

    return {
        "product": product.title,
        "current_price": current,
        "minimum_price": minimum,
        "maximum_price": maximum,
        "average_price": round(average, 2),
        "recommendation": recommendation,
        "confidence": confidence,
        "reason": reason,
        "target_price": minimum,
    }