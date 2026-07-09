from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class Product(Base):
    
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    url: Mapped[str] = mapped_column(
        String(1000),
        nullable=False,
    )

    store: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    image: Mapped[str] = mapped_column(
        String(1000),
        default="",
    )

    current_price: Mapped[float] = mapped_column(
        Float,
        default=0,
    )

    rating: Mapped[float] = mapped_column(
        Float,
        default=0,
    )

    reviews: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    user = relationship("User", back_populates="products")
    price_history = relationship(
    "PriceHistory",
    back_populates="product",
    cascade="all, delete-orphan",
)