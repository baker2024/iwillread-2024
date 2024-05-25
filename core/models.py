from typing import Optional

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from .db_manager import Base


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, unique=True)
    population = Column(Integer)


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]
    price: Mapped[int]
    count: Mapped[int]

