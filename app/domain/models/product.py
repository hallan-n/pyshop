import re

from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float

class ProductUpdate(ProductCreate):
    id: int = None

class Product(ProductUpdate):
    user_id: int