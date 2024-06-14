from domain.models.product import Product, ProductCreate, ProductUpdate
from domain.usecases.product_usecase import ProductUseCase
from fastapi import APIRouter, Depends
from infra.security import Security

use = ProductUseCase()
security = Security()
route = APIRouter(tags=["Product"], prefix="/product")


@route.post("/")
async def create_product(
    product: ProductCreate, token: dict = Depends(security.decode_token)
):
    return await use.create_product(
        Product(**product.model_dump(), user_id=token["id"])
    )


@route.put("/")
async def update_product(
    product: ProductUpdate, token: dict = Depends(security.decode_token)
):
    return await use.update_product(
        Product(**product.model_dump(), user_id=token["id"])
    )


@route.get("/")
async def read_all_products(token: dict = Depends(security.decode_token)):
    return await use.read_all_products(token["id"])


@route.get("/{id}")
async def read_product(id: int, token: dict = Depends(security.decode_token)):
    return await use.read_product(id, token["id"])


@route.delete("/{id}")
async def delete_product(id: int, token: dict = Depends(security.decode_token)):
    return await use.delete_product(id, token["id"])
