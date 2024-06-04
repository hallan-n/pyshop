from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    user_id: int


class Category(BaseModel):
    id: int
    name: str
    description: str
    product_id: int


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    is_seller: bool = False
