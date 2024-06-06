from sqlalchemy import (Boolean, Column, Float, ForeignKey, Integer, MetaData,
                        String, Table)

metadata = MetaData()

user_table = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255), nullable=False),
    Column("email", String(255), nullable=False, unique=True),
    Column("password", String(255), nullable=False),
    Column("is_seller", Boolean, nullable=False, default=False),
    extend_existing=True,
)

category_table = Table(
    "category",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255), nullable=False),
    Column("description", String(255), nullable=False),
    Column("product_id", Integer, ForeignKey("product.id"), nullable=False),
    extend_existing=True,
)

product_table = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255), nullable=False),
    Column("price", Float, nullable=False),
    Column("user_id", Integer, ForeignKey("user.id"), nullable=False),
    extend_existing=True,
)
