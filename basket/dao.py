from sqlalchemy import select, desc, delete, update, and_
from sqlalchemy.orm import joinedload, selectinload

from basket.models import CartItem
from dao.base import BaseDAO
from products.models import Product, Category
from database import async_session


class CartDAO(BaseDAO):
    model = CartItem

    @classmethod
    async def get_cart(cls, user_id: int):
        async with async_session() as session:
            query = (
                select(CartItem)
                .options(selectinload(CartItem.product))
                .where(CartItem.user_id == user_id)
            )
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def add_to_cart(cls, user_id: int, product_id: int, quantity: int):
        async with async_session() as session:
            existing_item = await cls.get_cart_item(user_id, product_id)
            if existing_item:
                await cls.add_to_cart_quantity(user_id, product_id, quantity)
            else:
                new_item = CartItem(
                    user_id=user_id, product_id=product_id, quantity=quantity
                )
                session.add(new_item)
            await session.commit()

    @classmethod
    async def update_cart_item(cls, user_id: int, product_id: int, quantity: int):
        async with async_session() as session:
            query = select(CartItem.__table__.columns).filter_by(
                user_id=user_id, product_id=product_id
            )
            existing_item = await session.execute(query)
            cart_item = existing_item.mappings().one()
            if cart_item:
                updated_values = {CartItem.quantity: quantity}
                await session.execute(
                    update(CartItem)
                    .where(
                        and_(
                            CartItem.user_id == user_id,
                            CartItem.product_id == product_id,
                        )
                    )
                    .values(updated_values)
                )
                await session.commit()
                return cart_item

        return None

    @classmethod
    async def add_to_cart_quantity(
        cls, user_id: int, product_id: int, quantity_to_add: int
    ):
        async with async_session() as session:
            query = select(CartItem.__table__.columns).filter_by(
                user_id=user_id, product_id=product_id
            )
            existing_item = await session.execute(query)
            cart_item = existing_item.mappings().one()
            if cart_item:
                updated_values = {
                    CartItem.quantity: cart_item.quantity + quantity_to_add
                }
                await session.execute(
                    update(CartItem)
                    .where(
                        and_(
                            CartItem.user_id == user_id,
                            CartItem.product_id == product_id,
                        )
                    )
                    .values(updated_values)
                )
                await session.commit()
                return cart_item

        return None

    @classmethod
    async def update_cart_quantity(cls, user_id: int, product_id: int, quantity: int):
        async with async_session() as session:
            query = select(CartItem.__table__.columns).filter_by(
                user_id=user_id, product_id=product_id
            )
            existing_item = await session.execute(query)
            cart_item = existing_item.mappings().one()
            if cart_item:
                updated_values = {CartItem.quantity: quantity}
                await session.execute(
                    update(CartItem)
                    .where(
                        and_(
                            CartItem.user_id == user_id,
                            CartItem.product_id == product_id,
                        )
                    )
                    .values(updated_values)
                )
                await session.commit()
                return cart_item

        return None

    @classmethod
    async def reduce_from_cart_quantity(
        cls, user_id: int, product_id: int, quantity_to_reduce: int
    ):
        async with async_session() as session:
            query = select(CartItem.__table__.columns).filter_by(
                user_id=user_id, product_id=product_id
            )
            existing_item = await session.execute(query)
            cart_item = existing_item.mappings().one()
            if cart_item and (cart_item.quantity - quantity_to_reduce >= 0):
                updated_values = {
                    CartItem.quantity: cart_item.quantity - quantity_to_reduce
                }
                await session.execute(
                    update(CartItem)
                    .where(
                        and_(
                            CartItem.user_id == user_id,
                            CartItem.product_id == product_id,
                        )
                    )
                    .values(updated_values)
                )
                await session.commit()
                return cart_item

        return None

    @classmethod
    async def delete_cart_item(cls, user_id: int, product_id: int):
        async with async_session() as session:
            existing_item = await cls.get_cart_item(user_id, product_id)
            if existing_item:
                query = delete(cls.model).where(
                    cls.model.user_id == user_id, cls.model.product_id == product_id
                )
                await session.execute(query)
                await session.commit()

    @classmethod
    async def get_cart_item(cls, user_id: int, product_id: int):
        async with async_session() as session:
            item = select(CartItem).filter_by(user_id=user_id, product_id=product_id)
            result = await session.execute(item)
            return result.first()

    @classmethod
    async def delete_cart(cls, user_id: int):
        async with async_session() as session:
            query = delete(cls.model).where(cls.model.user_id == user_id)
            await session.execute(query)
            await session.commit()
