from domain.models import User
from domain.usecases.user_usecase import UserUseCase
from fastapi import APIRouter

use = UserUseCase()

route = APIRouter(tags=["User"], prefix="/user")


@route.post("/")
async def sign_up(user: User):
    """Cria um usuário."""
    resp = await use.create_user(user)
    return resp


@route.put("/")
async def update_data(user: User):
    """Atualiza os dados de um usuário existente."""
    resp = await use.update_user(user)
    return resp


@route.get("/")
async def read_data(id: int):
    """Retorna os dados de um usuário."""
    resp = await use.get_user(id)
    return resp
