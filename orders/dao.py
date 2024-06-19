from sqlalchemy import select, desc, delete, update, and_
from sqlalchemy.orm import selectinload

from dao.base import BaseDAO
from orders.models import Order, OrderItem
from database import async_session


class OrderDAO(BaseDAO):
    model = Order

    @classmethod
    async def create_order(cls, user_id: int, total_price: float, items: list):
        async with async_session() as session:
            new_order = Order(user_id=user_id, total_price=total_price)
            session.add(new_order)
            await session.commit()

            for item in items:
                order_item = OrderItem(
                    order_id=new_order.id,
                    product_id=item["product_id"],
                    quantity=item["quantity"],
                    price=item["price"],
                )
                session.add(order_item)

            await session.commit()
            return new_order

    @classmethod
    async def get_order_info(cls, user_id: int, order_id: int):
        async with async_session() as session:
            item = select(Order).filter_by(user_id=user_id, id=order_id)
            result = await session.execute(item)
            return result.mappings().one()

    @classmethod
    async def get_orders_by_userid(cls, user_id: int):
        async with async_session() as session:
            query = (
                select(Order)
                .options(selectinload(Order.order_items))
                .where(Order.user_id == user_id)
                .order_by(desc(Order.created_at))
            )
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def get_orders_items_by_orderid(cls, order_id: int):
        async with async_session() as session:
            query = (
                select(OrderItem)
                .options(selectinload(OrderItem.product))
                .where(OrderItem.order_id == order_id)
            )
            result = await session.execute(query)
            order_items = []
            for row in result.mappings().all():
                order_items.append(row)
            return order_items

    @classmethod
    async def update_order_status(
        cls, user_id: int, order_id: int, new_status: int, decline_desc: str = None
    ):
        async with async_session() as session:
            async with session.begin():
                result = await session.execute(
                    select(Order).where(
                        and_(Order.id == order_id, Order.user_id == user_id)
                    )
                )
                order = result.scalar_one_or_none()

                if order:
                    update_values = {"status_id": new_status}
                    if decline_desc:
                        update_values["decline_desc"] = decline_desc

                    await session.execute(
                        update(Order)
                        .where(and_(Order.id == order_id, Order.user_id == user_id))
                        .values(**update_values)
                    )
                    await session.commit()
                    return {"message": "Order status updated successfully"}

                return {"message": "Order not found"}

    @classmethod
    async def del_order(cls, order_id: int):
        async with async_session() as session:
            query = delete(OrderItem).where(OrderItem.order_id == order_id)
            await session.execute(query)
            await session.commit()
            query = delete(Order).where(Order.id == order_id)
            await session.execute(query)
            await session.commit()
