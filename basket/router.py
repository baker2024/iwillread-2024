import json

from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from basket.dao import CartDAO
from basket.schemas import SCartItem, SCartDelete, SCartQuantity
from products.dao import ProductDAO
from products.models import Product
from basket.models import CartItem
from users.dependencies import get_current_user
from users.models import User

router = APIRouter(prefix="", tags=["Basket"])
templates = Jinja2Templates(directory="templates")


@router.get("/cart/{user_id}")
async def view_cart(user_id: int):
    cart = await CartDAO.get_cart(user_id)
    return cart


@router.post("/cart/add")
async def add_to_cart(data: SCartItem):
    await CartDAO.add_to_cart(data.user_id, data.product_id, data.quantity)
    return {"message": "Product added to cart"}


@router.put("/cart/quantity")
async def cart_quantity(data: SCartQuantity):
    if data.method == 'decrease_quantity':
        await CartDAO.reduce_from_cart_quantity(data.user_id, data.product_id, data.quantity)
        return {"message": "Cart item updated successfully"}
    elif data.method == 'increase_quantity':
        product = await ProductDAO.find_product_by_id(data.product_id)
        cart_item = await CartDAO.get_cart_item(data.user_id, data.product_id)
        if product.count > cart_item.CartItem.quantity:
            await CartDAO.add_to_cart_quantity(data.user_id, data.product_id, data.quantity)
            return {"message": "Cart item updated successfully"}
        else:
            return {"message": "Такого количества нет в наличии"}


@router.delete("/cart/delete")
async def delete_cart_item(data: SCartDelete):
    await CartDAO.delete_cart_item(data.user_id, data.product_id)
    return {"message": "Cart item deleted successfully"}


@router.get("/basket")
async def get_basket_page(request: Request, user: User = Depends(get_current_user)):
    if not user:
        return RedirectResponse("/login")
    items = await CartDAO.get_cart(user.id)
    total_price = 0
    if items:
        for item in items:
            if item.CartItem.product:
                total_price += item.CartItem.product.price * item.CartItem.quantity
            else:
                await CartDAO.delete_cart_item(user.id, item.CartItem.product_id)
    return templates.TemplateResponse("basket.html",
                                      {"request": request, "user": user, "items": items, "total_price": total_price})


