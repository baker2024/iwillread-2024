from datetime import datetime

from sqlalchemy import ForeignKey, DateTime, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    total_price: Mapped[float] = mapped_column(Float)
    status_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("order_status.id"), default=1
    )
    adress: Mapped[str] = mapped_column(nullable=True)
    decline_desc: Mapped[str] = mapped_column(nullable=True)
    user = relationship("User", back_populates="orders", lazy="selectin")
    order_items = relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete-orphan",
        lazy="selectin",
    )
    status = relationship("OrderStatus", back_populates="orders", lazy="selectin")

    def __str__(self):
        return f"ID: {self.id} USER: {self.user_id} TOTAL-PRICE: {self.total_price} STATUS: {self.status}"


class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    order_id: Mapped[int] = mapped_column(Integer, ForeignKey("orders.id"))
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"))
    quantity: Mapped[int] = mapped_column(Integer)
    price: Mapped[float] = mapped_column(Float)

    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items", lazy="selectin")

    def __str__(self):
        return f"Товар: {self.product}, Количество: {self.quantity} шт., Цена: {self.price} РУБ"


class OrderStatus(Base):
    __tablename__ = "order_status"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    orders = relationship("Order", back_populates="status")

    def __str__(self):
        return f"{self.name}"
