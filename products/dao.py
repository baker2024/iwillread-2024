from sqlalchemy import select

from dao.base import BaseDAO
from products.models import Product, Category
from database import async_session


class ProductDAO(BaseDAO):
    model = Product

    @classmethod
    async def find_all_with_images(cls):
        async with async_session() as session:
            query = (
                select(
                    Product.__table__.columns
                )
            )
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def find_product_by_id(cls, product_id: int):
        async with async_session() as session:
            query = (
                select(
                    Product.__table__.columns
                )
                .where(Product.id == product_id)
            )
            result = await session.execute(query)
            return result.mappings().one()

    @classmethod
    async def find_all_categories(cls):
        async with async_session() as session:
            query = (
                select(
                    Category.__table__.columns
                )
            )
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def find_all_by_category(cls, category_id: int):
        async with async_session() as session:
            query = (
                select(
                    Product.__table__.columns
                )
                .where(Product.category_id == category_id)
            )
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def find_category_by_id(cls, category_id: int):
        async with async_session() as session:
            query = (
                select(
                    Category.__table__.columns
                )
                .where(Category.id == category_id)
            )
            result = await session.execute(query)
            return result.mappings().one()


