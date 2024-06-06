from typing import Optional, List

from pydantic import BaseModel


class ProductBase(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: int
    count: int
    image: Optional[str] = None

