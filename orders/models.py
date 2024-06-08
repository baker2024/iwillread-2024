from datetime import datetime

from sqlalchemy import Column, ForeignKey, DateTime, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    total_price: Mapped[float] = mapped_column(Float)
    status: Mapped[str] = mapped_column(default="Новый")

    user = relationship("User", back_populates="orders", lazy="selectin")
    order_items = relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete-orphan",
        lazy="selectin",
    )

    def __str__(self):
        return f"ID: {self.id} USER: {self.user_id} TOTAL-PRICE: {self.total_price} STATUS: {self.status}"


class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    order_id: Mapped[int] = mapped_column(Integer, ForeignKey("orders.id"))
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"))
    quantity: Mapped[int] = mapped_column(Integer)
    price: Mapped[float]

    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items", lazy="selectin")

    def __str__(self):
        return f"Товар: {self.product}, Количество: {self.quantity} шт., Цена: {self.price} РУБ"
