import json

from domain.models import Product
from fastapi import Response, status
from fastapi.exceptions import HTTPException
from infra.repositories import Repositories
from infra.schemas import product_table, user_table
from infra.security import Security


class ProductUseCase:
    def __init__(self):
        self.repo = Repositories()
        self.security = Security()

    async def create_product(self, product: Product):
        is_seller = await self.repo.execute_sql(
            f"SELECT 1 FROM user WHERE id={product.user_id} AND is_seller=1"
        )
        if is_seller == []:
            raise HTTPException(
                detail="O usuário não é um vendedor",
                status_code=status.HTTP_409_CONFLICT,
            )
        created = await self.repo.create(product_table, product.model_dump())
        response = json.dumps({"sucess": created})
        return Response(content=response, status_code=status.HTTP_201_CREATED)

    async def update_user(self, product: Product):
        stmt = await self.repo.execute_sql(
            f'SELECT 1 FROM product WHERE id="{product.id}"'
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

    async def read_product(self, id: int):
        product = await self.repo.read(product_table, id)
        if product == [] or not product:
            raise HTTPException(
                detail="Produto não encontrado.", status_code=status.HTTP_404_NOT_FOUND
            )
        return Product(**product)

    async def read_all_products(self):
        products = await self.repo.read_all(product_table)
        if products == []:
            raise HTTPException(
                detail="Não existe produtos.", status_code=status.HTTP_404_NOT_FOUND
            )
        return products

    async def delete_products(self, id: int):
        product_existes = await self.repo.execute_sql(
            f"SELECT 1 FROM product WHERE id={id}"
        )
        if product_existes == []:
            raise HTTPException(
                detail="Produto não encontrado.", status_code=status.HTTP_404_NOT_FOUND
            )

        deleted = await self.repo.delete(product_table, id)
        response = json.dumps({"sucess": deleted})
        return Response(content=response, status_code=status.HTTP_200_OK)
