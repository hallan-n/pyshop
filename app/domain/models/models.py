import re

from pydantic import BaseModel




class Category(BaseModel):
    id: int = None
    name: str
    description: str
    product_id: int
