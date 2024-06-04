from app.infra.repositories import Repositories
from app.infra.schemas import user_table
from app.domain.models import User

class UserUseCase:
    def __init__(self):
        self.repo = Repositories()

    async def create_user(self, user: User):
        ...

    async def update_user(self, user: User):
        ...

    async def get_user(self, id: int):
        ...