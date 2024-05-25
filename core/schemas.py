from typing import Optional
from pydantic import BaseModel, ConfigDict


class SProductAdd(BaseModel):
    name: str
    description: Optional[str]
    price: int
    count: int

class SProduct(SProductAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)

class SProductId(BaseModel):
    ok: bool = True
    product_id: int