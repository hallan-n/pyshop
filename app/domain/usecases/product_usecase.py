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
        is_seller = await self.repo.execute_sql(f'SELECT 1 FROM user WHERE id={product.user_id} AND is_seller=1')
        if is_seller == []:
            raise HTTPException(
                detail="O usuário não é um vendedor", status_code=status.HTTP_409_CONFLICT
            )
        created = await self.repo.create(product_table, product.model_dump())        
        response = json.dumps({"sucess": created})
        return Response(content=response, status_code=status.HTTP_201_CREATED)