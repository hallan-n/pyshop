from pydantic import BaseModel, field_validator


class Product(BaseModel):
    id: int = None
    name: str
    price: float
    user_id: int


class Category(BaseModel):
    id: int = None
    name: str
    description: str
    product_id: int


class User(BaseModel):
    id: int = None
    name: str
    email: str
    password: str
    is_seller: bool = False
