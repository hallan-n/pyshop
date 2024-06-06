import re

from pydantic import BaseModel, Field, field_validator


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

    @field_validator("name", "email", "password")
    def lenght_validate(cls, value, field: Field):
        if not (4 <= len(value) <= 254):
            raise ValueError(
                f"O campo {field.field_name.capitalize()} deve ter entre 4 e 254 caracteres."
            )
        return value

    @field_validator("email")
    def email_validate(cls, value):
        if not re.match(".+@.+\\.[a-zA-Z]{2}", value.lower()):
            raise ValueError(f"O campo Email não está no padrão aceito.")
        return value.lower()


class UserPassword(BaseModel):
    id: int
    new_password: str
    old_password: str

    @field_validator("old_password", "new_password")
    def lenght_validate(cls, value, field: Field):
        if not (4 <= len(value) <= 254):
            raise ValueError(
                f"O campo {field.field_name.capitalize()} deve ter entre 4 e 254 caracteres."
            )
        return value
