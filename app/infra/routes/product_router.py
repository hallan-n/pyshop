from domain.models import Product, ProductReadDelete
from domain.usecases.product_usecase import ProductUseCase
from fastapi import APIRouter, Depends, HTTPException, status
from infra.security import Security

use = ProductUseCase()
security = Security()
route = APIRouter(tags=["Product"], prefix="/product")


@route.post("/")
async def create_product(product: Product, token: dict = Depends(security.decode_token)):
    
    if not use.is_owner(product.id, token):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return await use.create_product(product)

@route.put("/")
async def update_product(product: Product, token: dict = Depends(security.decode_token)):
    if not use.is_owner(product.id, token):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return await use.update_product(product)

@route.get("/")
async def read_all_products(token: dict = Depends(security.decode_token)
):
    return await use.read_all_products(token['id'])

@route.get("/{id}")
async def read_product(id: int, token: dict = Depends(security.decode_token)
):
    if not use.is_owner(id, token):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return await use.read_product(id, token['id'])


@route.delete("/{id}")
async def delete_products(id: int, token: dict = Depends(security.decode_token)):
    if not use.is_owner(id, token):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return await use.delete_product(id, token['id'])
