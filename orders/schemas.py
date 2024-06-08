from typing import List

from pydantic import BaseModel


class SOrder(BaseModel):
    user_id: int
    items: list
    total_price: str

