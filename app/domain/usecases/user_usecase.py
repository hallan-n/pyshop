from infra.repositories import Repositories
from infra.schemas import user_table
from domain.models import User
from pydantic import ValidationError
from fastapi.exceptions import HTTPException

class UserUseCase:
    def __init__(self):
        self.repo = Repositories()

    async def create_user(self, user: User):
        # SELECT EXISTS (SELECT 1 FROM user WHERE email="exemplo@email.com");
        ...    

    async def update_user(self, user: User):
        ...

    async def get_user(self, id: int):
        ...