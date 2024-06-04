from infra.repositories import Repositories

class UserUseCase:
    def __init__(self):
        self.repo = Repositories()

    async def create_user(self):
        ...

    async def update_user(self):
        ...

    async def get_user(self):
        ...