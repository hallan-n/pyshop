from pydantic import BaseModel, Field, field_validator


class ProductCreate(BaseModel):
    name: str
    price: float

    @field_validator("name")
    def lenght_validator(cls, value, field: Field):
        if not (4 <= len(value) <= 254):
            raise ValueError(
                f"O campo {field.field_name.capitalize()} deve ter entre 4 e 254 caracteres."
            )
        return value


class ProductUpdate(ProductCreate):
    id: int = None


class Product(ProductUpdate):
    user_id: int
