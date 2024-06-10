import re

from pydantic import BaseModel, Field, field_validator


class Product(BaseModel):
    id: int = None
    name: str
    price: float
    user_id: int


class ProductReadDelete(BaseModel):
    product_id: int
    user_id: int


class Category(BaseModel):
    id: int = None
    name: str
    description: str
    product_id: int
