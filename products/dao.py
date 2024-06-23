from sqlalchemy import select, desc
from sqlalchemy.orm import selectinload

from dao.base import BaseDAO
from products.models import Author, Product, Category
from database import async_session


class ProductDAO(BaseDAO):
    model = Product

    @classmethod
    async def find_all_with_images(cls):
        async with async_session() as session:
            query = select(Product.__table__.columns).order_by(desc(Product.created_at))
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def find_all_filter(cls, category_id: int = None, sort_by: str = None):
        async with async_session() as session:
            query = select(Product.__table__.columns)

            if category_id:
                query = query.where(Product.category_id == category_id)

            if sort_by == "price_desc":
                query = query.order_by(Product.price.desc())
            elif sort_by == "density_desc":
                query = query.order_by(Product.density.desc())
            elif sort_by == "width_desc":
                query = query.order_by(Product.width.desc())
            elif sort_by == "density_asc":
                query = query.order_by(Product.density.asc())
            elif sort_by == "width_asc":
                query = query.order_by(Product.width.asc())
            elif sort_by == "price_asc":
                query = query.order_by(Product.density.asc())
            else:
                query = query.order_by(desc(Product.created_at))

            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def find_product_by_id(cls, product_id: int):
        async with async_session() as session:
            query = select(Product.__table__.columns).where(Product.id == product_id)
            result = await session.execute(query)
            return result.mappings().one()

    @classmethod
    async def find_author_by_id(cls, id: int):
        async with async_session() as session:
            query = select(Author.__table__.columns).where(Author.id == id)
            result = await session.execute(query)
            return result.mappings().one()

    @classmethod
    async def find_all_authors(
        cls,
    ):
        async with async_session() as session:
            query = select(Author.__table__.columns)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def search(cls, query: str):
        async with async_session() as session:
            # Начинаем асинхронную транзакцию
            async with session.begin():
                # Поиск книг по названию и загрузка связанных авторов
                books_query = (
                    select(Product)
                    .filter(Product.name.ilike(f"%{query}%"))
                    .options(selectinload(Product.author))
                )
                books_result = await session.execute(books_query)
                books = [book for book in books_result.scalars()]

                # Поиск авторов по имени
                authors_query = select(Author).filter(Author.name.ilike(f"%{query}%"))
                authors_result = await session.execute(authors_query)
                authors = [author for author in authors_result.scalars()]

        # Возвращаем результаты поиска
        results = books + authors
        return results

    @classmethod
    async def find_all_by_author_id(cls, author_id: int):
        async with async_session() as session:
            query = (
                select(Product.__table__.columns)
                .order_by(desc(Product.created_at))
                .where(Product.author_id == author_id)
            )
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def find_all_categories(cls):
        async with async_session() as session:
            query = select(Category.__table__.columns)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def find_all_by_category(cls, category_id: int):
        async with async_session() as session:
            query = (
                select(Product.__table__.columns)
                .order_by(desc(Product.created_at))
                .where(Product.category_id == category_id)
            )
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def find_all_by_categoryname(cls, category: str):
        async with async_session() as session:
            query = (
                select(Product.__table__.columns)
                .order_by(desc(Product.created_at))
                .where(Product.category_id == category)
            )
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def find_category_by_id(cls, category_id: int):
        async with async_session() as session:
            query = select(Category.__table__.columns).where(Category.id == category_id)
            result = await session.execute(query)
            return result.mappings().one()

    @classmethod
    async def find_latests_five(cls):
        async with async_session() as session:
            query = (
                select(Product.__table__.columns)
                .order_by(desc(Product.created_at))
                .limit(5)
            )
            result = await session.execute(query)
            return result.mappings().all()
