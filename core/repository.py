from sqlalchemy import select

from .db_manager import async_session
from .models import Product
from .schemas import SProduct, SProductAdd


class ProductRepository:
    @classmethod
    async def add_one(cls, data: SProductAdd) -> int:
        async with async_session() as session:
            product_dict = data.model_dump()

            product = Product(**product_dict)
            session.add(product)
            await session.flush()
            await session.commit()
            return product.id

    @classmethod
    async def find_all(cls) -> list[SProduct]:
        async with async_session() as session:
            query = select(Product)
            result = await session.execute(query)
            product_models = result.scalars().all()
            product_schemas = [SProduct.model_validate(product_model) for product_model in product_models]
            return product_schemas
        
    @classmethod
    async def find_by_id(cls, id) -> list[SProduct]:
        async with async_session() as session:
            product = await session.get(Product, id)
            return product