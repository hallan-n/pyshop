import json

from domain.models import User
from fastapi import Response, status
from fastapi.exceptions import HTTPException
from infra.repositories import Repositories
from infra.schemas import user_table


class UserUseCase:
    def __init__(self):
        self.repo = Repositories()

    async def create_user(self, user: User):
        stmt = await self.repo.execute_sql(
            f'SELECT 1 FROM user WHERE email="{user.email}"'
        )
        if stmt != []:
            raise HTTPException(
                detail="E-mail já cadastrado.", status_code=status.HTTP_409_CONFLICT
            )
        created = await self.repo.create(user_table, user.model_dump())
        response = json.dumps({"sucess": created})
        return Response(content=response, status_code=status.HTTP_201_CREATED)

    async def update_user(self, user: User):
        stmt = await self.repo.execute_sql(f'SELECT 1 FROM user WHERE id="{user.id}"')
        if stmt == []:
            raise HTTPException(
                detail="Usuário não encontrado.", status_code=status.HTTP_404_NOT_FOUND
            )
        stmt = await self.repo.execute_sql(
            f'SELECT 1 FROM user WHERE email="{user.email}"'
        )
        if stmt != []:
            raise HTTPException(
                detail="O Email já está em uso.", status_code=status.HTTP_409_CONFLICT
            )

        updated = await self.repo.update(user_table, user.model_dump())
        response = json.dumps({"sucess": updated})
        return Response(content=response, status_code=status.HTTP_200_OK)

    async def get_user(self, id: int):
        stmt = await self.repo.read(user_table, id)
        if stmt == None:
            raise HTTPException(
                detail="Usuário não encontrado.", status_code=status.HTTP_404_NOT_FOUND
            )
        return User(**stmt)
