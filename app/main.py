from app.domain.usecases.user_usecase import UserUseCase
from app.domain.models import User
from fastapi import FastAPI

use = UserUseCase()

app = FastAPI()

@app.post('/')
async def main(user: User):
    await use.create_user(user)