from sqlalchemy.orm import Session

from app.models.product import Product
from app.models.price_history import PriceHistory
from app.models.user import User

from app.scrapers.scraper_factory import get_scraper


def import_product(
    db: Session,
    url: str,
    current_user: User,
):
    scraper = get_scraper(url)

    data = scraper.extract(url)

    if not data["title"]:
        raise ValueError("Unable to scrape product.")

    existing_product = (
    db.query(Product)
    .filter(
        Product.user_id == current_user.id,
        Product.title == data["title"],
    )
    .first()
)

    if existing_product:

        existing_product.current_price = data["price"]
        existing_product.rating = data["rating"]
        existing_product.reviews = data["reviews"]

        if data["image"]:
            existing_product.image = data["image"]

        db.commit()

        history = PriceHistory(
            product_id=existing_product.id,
            price=data["price"],
        )

        db.add(history)
        db.commit()

        return existing_product

    store = url.split(".")[1].capitalize()

    product = Product(
        user_id=current_user.id,
        title=data["title"],
        url=url,
        store=store,
        image=data["image"],
        current_price=data["price"],
        rating=data["rating"],
        reviews=data["reviews"],
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    history = PriceHistory(
        product_id=product.id,
        price=data["price"],
    )

    db.add(history)
    db.commit()

    return product