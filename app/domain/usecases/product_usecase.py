import json

from domain.models.product import Product
from fastapi import Response, status
from fastapi.exceptions import HTTPException
from infra.repositories import Repositories
from infra.schemas import product_table
from infra.security import Security


class ProductUseCase:
    def __init__(self):
        self.repo = Repositories()
        self.security = Security()

    async def create_product(self, product: Product):
        created = await self.repo.create(product_table, product.model_dump())
        response = json.dumps({"sucess": created})
        return Response(content=response, status_code=status.HTTP_201_CREATED)

    async def update_product(self, product: Product):
        stmt = await self.repo.execute_sql(
            f'SELECT 1 FROM product WHERE id={product.id}'
        )
        if stmt == []:
            raise HTTPException(
                detail="Produto não encontrado.", status_code=status.HTTP_404_NOT_FOUND
            )
        updated = await self.repo.update(product_table, product.model_dump())
        if not updated:
            raise HTTPException(
                detail="Erro ao atualizar os dados do produto.",
                status_code=status.HTTP_409_CONFLICT,
            )
        response = json.dumps({"sucess": updated})
        return Response(content=response, status_code=status.HTTP_200_OK)

    async def read_product(self, product_id: int, owner:int):
        product_existes = await self.repo.execute_sql(f'SELECT 1 FROM product WHERE id={product_id} AND user_id={owner}')
        if product_existes == []:
            raise HTTPException(
                detail="Produto não encontrado.", status_code=status.HTTP_404_NOT_FOUND
            )
        product = await self.repo.execute_sql(f'SELECT * FROM product WHERE id={product_id} AND user_id={owner}')
        return Product(**product[0])

    async def read_all_products(self, user_id: int):
        products = await self.repo.execute_sql(f'SELECT * FROM product WHERE user_id={user_id}')
        if products == []:
            raise HTTPException(
                detail="Não existe produtos.", status_code=status.HTTP_404_NOT_FOUND
            )
        return products

    async def delete_product(self, product_id: int, owner:int):
        product_existes = await self.repo.execute_sql(f'SELECT 1 FROM product WHERE id={product_id} AND user_id={owner}')
        if product_existes == []:
            raise HTTPException(
                detail="Produto não encontrado.", status_code=status.HTTP_404_NOT_FOUND
            )
        deleted = await self.repo.delete(product_table, product_id)
        response = json.dumps({"sucess": deleted})
        return Response(content=response, status_code=status.HTTP_200_OK)

    async def is_seller(self, token: dict):
        seller = await self.repo.execute_sql(f'SELECT 1 FROM product WHERE id={token['id']} AND is_seller=1')
        return bool(seller)
