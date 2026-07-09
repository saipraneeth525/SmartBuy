from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate


def create_product(
    db: Session,
    user_id: int,
    product: ProductCreate,
):
    db_product = Product(
        user_id=user_id,
        title=product.title,
        url=product.url,
        store=product.store,
        image=product.image,
        current_price=product.current_price,
        rating=product.rating,
        reviews=product.reviews,
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


def get_products(
    db: Session,
    user_id: int,
):
    return (
        db.query(Product)
        .filter(Product.user_id == user_id)
        .all()
    )


def get_product(
    db: Session,
    product_id: int,
    user_id: int,
):
    return (
        db.query(Product)
        .filter(
            Product.id == product_id,
            Product.user_id == user_id,
        )
        .first()
    )


def delete_product(
    db: Session,
    product: Product,
):
    db.delete(product)
    db.commit()