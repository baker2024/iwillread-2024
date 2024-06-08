import json

from fastapi import APIRouter, Depends, Request, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from basket.dao import CartDAO
from basket.schemas import SCartItem, SCartDelete, SCartQuantity
from orders.dao import OrderDAO
from orders.models import Order
from orders.schemas import SOrder
from products.dao import ProductDAO
from products.models import Product
from basket.models import CartItem
from users.dependencies import get_current_user
from users.models import User

router = APIRouter(prefix="", tags=["Order"])
templates = Jinja2Templates(directory="templates")


@router.post("/orders")
async def create_order(
    request: Request, data: SOrder, user: User = Depends(get_current_user)
):
    if user:
        items = data.items
        total_price = float(data.total_price)
        for item in items:
            product_id = item["product_id"]
            product = await ProductDAO.find_product_by_id(product_id)
            item["price"] = product.price

        result = await OrderDAO.create_order(user.id, total_price, items)

        if not items:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="No items in the order"
            )
        return result


@router.get("/my-orders/")
async def get_order(request: Request, user: User = Depends(get_current_user)):
    if user:
        orders = await OrderDAO.get_orders_by_userid(user.id)
        order_items_list = []
        for order in orders:
            order_items = await OrderDAO.get_orders_items_by_orderid(order.Order.id)
            for order_item in order_items:
                product = order_item.OrderItem.product
                order_item_info = {
                    "product_name": product.name,
                    "price": product.price,
                    "image": product.image,
                    "quantity": order_item.OrderItem.quantity,
                }
                order_items_list.append(order_item_info)
        return templates.TemplateResponse(
            "orders.html",
            {
                "request": request,
                "orders": orders,
                "user": user,
                "order_items": order_items_list,
            },
        )
    return RedirectResponse("/login")


@router.get("/orders/{order_id}")
async def get_order(order_id: int, user: User = Depends(get_current_user)):
    if user:
        result = await OrderDAO.get_order_info(user.id, order_id)
        return result


@router.put("/orders/{order_id}/status")
async def update_order_status(
    order_id: int, new_status: str, user: User = Depends(get_current_user)
):
    if user:
        await OrderDAO.update_order_status(user.id, order_id, new_status)
        return {"message": "Order status updated successfully"}


@router.put("/orders/del/{order_id}")
async def delete_order(order_id: int, user: User = Depends(get_current_user)):
    if user:
        await OrderDAO.update_order_status(user.id, order_id, "Отменен пользователем.")
        return {"message": "Order status updated successfully"}
