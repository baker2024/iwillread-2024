from typing import List

from pydantic import BaseModel


class SCartItem(BaseModel):
    user_id: int
    product_id: int
    quantity: int


class SCartQuantity(BaseModel):
    user_id: int
    product_id: int
    quantity: int
    method: str


class Cart(BaseModel):
    user_id: str
    items: List[SCartItem]


class SCartDelete(BaseModel):
    user_id: int
    product_id: int
