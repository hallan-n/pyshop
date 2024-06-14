import json

from domain.models.user import User, UserCreate, UserLogin, UserPassword, UserUpdate
from fastapi import Response, status
from fastapi.exceptions import HTTPException
from infra.repositories import Repositories
from infra.schemas import user_table
from infra.security import Security


class UserUseCase:
    def __init__(self):
        self.repo = Repositories()
        self.security = Security()

    async def create_user(self, user: UserCreate):
        stmt = await self.repo.execute_sql(
            f'''
                SELECT 1 FROM user
                WHERE email="{user.email}"
            '''
        )
        if stmt != []:
            raise HTTPException(
                detail="E-mail já cadastrado.", status_code=status.HTTP_409_CONFLICT
            )
        user.password = self.security.hashed(user.password)
        created = await self.repo.create(user_table, user.model_dump())
        response = json.dumps({"sucess": created})
        return Response(content=response, status_code=status.HTTP_201_CREATED)

    async def update_user(self, user: UserUpdate, user_id: int):
 
        stmt = await self.repo.execute_sql(
            f'''
                SELECT 1 FROM user
                WHERE email="{user.email}"
                AND id <> {user_id}
            '''
        )
        if stmt != []:
            raise HTTPException(
                detail="O Email já está em uso.", status_code=status.HTTP_409_CONFLICT
            )
        updated = await self.repo.execute_sql(
            f'''
                UPDATE user
                SET name="{user.name}",
                email="{user.email}",
                is_seller={user.is_seller}
                WHERE id={user_id}
            '''
        )
        if not updated:
            raise HTTPException(
                detail="Erro ao atualizar os dados do usuário.",
                status_code=status.HTTP_409_CONFLICT,
            )

        response = json.dumps({"sucess": updated})
        return Response(content=response, status_code=status.HTTP_200_OK)

    async def update_password(self, user: UserPassword, user_id: int):
        current_pass = await self.repo.execute_sql(
            f'''
                SELECT password
                FROM user
                WHERE id={user_id}
            '''
        )
        if not self.security.check_hash(current_pass[0]["password"], user.old_password):
            raise HTTPException(
                detail="Senha incorreta.",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        user.new_password = self.security.hashed(user.new_password)
        updated = await self.repo.execute_sql(
            f'''
                UPDATE user
                SET password="{user.new_password}"
                WHERE id={user_id}
            '''
        )
        if not updated:
            raise HTTPException(
                detail="Erro ao atualizar os dados do usuário.",
                status_code=status.HTTP_409_CONFLICT,
            )
        
        response = json.dumps({"sucess": updated})
        return Response(content=response, status_code=status.HTTP_200_OK)

    async def get_user_by_id(self, id: int):
        stmt = await self.repo.read(user_table, id)
        if stmt == None:
            raise HTTPException(
                detail="Usuário não encontrado.", status_code=status.HTTP_404_NOT_FOUND
            )
        return User(**stmt)

    async def get_user_by_login(self, user: UserLogin):
        stmt = await self.repo.execute_sql(
            f'SELECT 1 FROM user WHERE email="{user.email}"'
        )
        if stmt == []:
            raise HTTPException(
                detail="Usuário não encontrado.", status_code=status.HTTP_404_NOT_FOUND
            )
        stmt = await self.repo.execute_sql(
            f'SELECT * FROM user WHERE email="{user.email}"'
        )
        if not self.security.check_hash(stmt[0]["password"], user.password):
            raise HTTPException(
                detail="Senha incorreta.",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        return User(**stmt[0])

    async def get_user_by_email(self, email: str):
        stmt = await self.repo.execute_sql(
            f'SELECT 1 FROM user WHERE email="{email}"'
        )
        if stmt == []:
            raise HTTPException(
                detail="Usuário não encontrado.", status_code=status.HTTP_404_NOT_FOUND
            )
        stmt = await self.repo.execute_sql(
            f'SELECT * FROM user WHERE email="{email}"'
        )
        return User(**stmt[0])
