from datetime import datetime
from typing import Optional

from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import FileType
from sqlalchemy import Column, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


storage = FileSystemStorage(path="static/img")


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    products = relationship("Product", back_populates="category")

    def __str__(self):
        return f"{self.name}"


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    image = Column(FileType(storage=storage))
    description: Mapped[Optional[str]] = mapped_column(nullable=True)
    products = relationship("Product", back_populates="author")

    def __str__(self):
        return f"{self.name}"


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"), nullable=False
    )
    category = relationship("Category", back_populates="products", lazy="selectin")
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[Optional[str]] = mapped_column(nullable=True)
    price: Mapped[int] = mapped_column(nullable=False)
    count: Mapped[int] = mapped_column(nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"), nullable=False)
    author = relationship("Author", back_populates="products", lazy="selectin")
    year: Mapped[Optional[str]] = mapped_column(nullable=True)
    years_old: Mapped[Optional[str]] = mapped_column(nullable=True)
    count_pages: Mapped[Optional[int]] = mapped_column(nullable=True)
    image = Column(FileType(storage=storage))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    cart_items = relationship("CartItem", back_populates="product")
    order_items = relationship("OrderItem", back_populates="product")

    def __str__(self):
        return f"{self.name}"
