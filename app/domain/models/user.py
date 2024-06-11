import re

from pydantic import BaseModel, Field, field_validator


class UserLogin(BaseModel):
    email: str
    password: str

    @field_validator("email")
    def email_validate(cls, value):
        if not re.match(".+@.+\\.[a-zA-Z]{2}", value.lower()):
            raise ValueError(f"O campo Email não está no padrão aceito.")
        return value.lower()

    @field_validator("email", "password")
    def lenght_validator(cls, value, field: Field):
        if not (4 <= len(value) <= 254):
            raise ValueError(
                f"O campo {field.field_name.capitalize()} deve ter entre 4 e 254 caracteres."
            )
        return value


class UserCreate(UserLogin):
    name: str
    is_seller: bool = False

    @field_validator("name")
    def lenght_validator(cls, value, field: Field):
        if not (4 <= len(value) <= 254):
            raise ValueError(
                f"O campo {field.field_name.capitalize()} deve ter entre 4 e 254 caracteres."
            )
        return value


class UserUpdate(BaseModel):
    id: int = None
    name: str
    email: str
    is_seller: bool

    @field_validator("email")
    def email_validate(cls, value):
        if not re.match(".+@.+\\.[a-zA-Z]{2}", value.lower()):
            raise ValueError(f"O campo Email não está no padrão aceito.")
        return value.lower()

    @field_validator("name", "email")
    def name_validator(cls, value, field: Field):
        if not (4 <= len(value) <= 254):
            raise ValueError(
                f"O campo {field.field_name.capitalize()} deve ter entre 4 e 254 caracteres."
            )
        return value


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


class User(UserUpdate):
    password: str

    @field_validator("password")
    def lenght_validate(cls, value, field: Field):
        if not (4 <= len(value) <= 254):
            raise ValueError(
                f"O campo {field.field_name.capitalize()} deve ter entre 4 e 254 caracteres."
            )
        return value
