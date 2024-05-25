from typing import List, Optional
from sqlalchemy import delete, select, update

from .db_manager import async_session
from .models import Category, Product
from .schemas import SCategory, SCategoryAdd, SProduct, SProductAdd


class ProductRepository:
    @classmethod
    async def add_one(cls, data: SProductAdd) -> Optional[int]:
        async with async_session() as session:
            category = await session.get(Category, data.category_id)
            if not category:
                return None

            product_dict = data.model_dump()

            product = Product(**product_dict)
            session.add(product)
            await session.flush()
            await session.commit()
            return product.id

    @classmethod
    async def delete_by_id(cls, id: int) -> bool:
        async with async_session() as session:
            stmt = delete(Product).where(Product.id == id)
            result = await session.execute(stmt)
            await session.commit()
            return result.rowcount > 0

    @classmethod
    async def update(cls, id: int, data: SProductAdd) -> bool:
        async with async_session() as session:
            category = await session.get(Category, data.category_id)
            if not category:
                return False

            product_dict = data.model_dump()

            stmt = (
                update(Product)
                .where(Product.id == id)
                .values(**product_dict)
            )
            result = await session.execute(stmt)
            await session.commit()
            return result.rowcount > 0

    @classmethod
    async def find_all(cls) -> List[SProduct]:
        async with async_session() as session:
            query = select(Product)
            result = await session.execute(query)
            product_models = result.scalars().all()
            product_schemas = [SProduct.model_validate(product_model) for product_model in product_models]
            return product_schemas
        
    @classmethod
    async def find_all_by_category_id(cls, category_id: int) -> List[SProduct]:
        async with async_session() as session:
            query = select(Product).where(Product.category_id == category_id)
            result = await session.execute(query)
            product_models = result.scalars().all()
            product_schemas = [SProduct.parse_obj(product_model.__dict__) for product_model in product_models]
            return product_schemas

    @classmethod
    async def find_by_id(cls, id: int) -> Optional[SProduct]:
        async with async_session() as session:
            product = await session.get(Product, id)
            if product:
                return SProduct.model_validate(product)
            return None        


class CategoryRepository:
    @classmethod
    async def add_one(cls, data: SCategoryAdd) -> int:
        async with async_session() as session:
            category_dict = data.model_dump()

            category = Category(**category_dict)
            session.add(category)
            await session.flush()
            await session.commit()
            return category.id

    @classmethod
    async def delete_by_id(cls, id: int) -> bool:
        async with async_session() as session:
            stmt = delete(Category).where(Category.id == id)
            result = await session.execute(stmt)
            await session.commit()
            return result.rowcount > 0

    @classmethod
    async def update(cls, id: int, data: SCategoryAdd) -> bool:
        async with async_session() as session:
            stmt = (
                update(Category)
                .where(Category.id == id)
                .values(**data.model_dump())
            )
            result = await session.execute(stmt)
            await session.commit()
            return result.rowcount > 0

    @classmethod
    async def find_all(cls):
        async with async_session() as session:
            query = select(Category)
            result = await session.execute(query)
            category_models = result.scalars().all()
            category_schemas = [category_model for category_model in category_models]
            return category_schemas

    @classmethod
    async def find_by_id(cls, id: int) -> SCategory:
        async with async_session() as session:
            category = await session.get(Category, id)
            if category:
                return SCategory.model_validate(category)
            return None


