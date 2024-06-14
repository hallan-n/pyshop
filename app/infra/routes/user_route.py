from domain.models.user import UserCreate, UserPassword, UserUpdate
from domain.usecases.user_usecase import UserUseCase
from fastapi import APIRouter, Depends
from infra.security import Security

use = UserUseCase()
security = Security()
route = APIRouter(tags=["User"], prefix="/user")


@route.post("/")
async def sign_up(user: UserCreate):
    """Cria um usuário."""
    return await use.create_user(user)


@route.put("/")
async def update_data(user: UserUpdate, token: dict = Depends(security.decode_token)):
    """Atualiza os dados de um usuário existente."""
    return await use.update_user(user, user_id=token["id"])


@route.put("/pass")
async def update_password(
    user: UserPassword, token: dict = Depends(security.decode_token)
):
    """Atualiza a senha de um usuário existente."""
    return await use.update_password(user, token["id"])


@route.get("/")
async def read_data(token: dict = Depends(security.decode_token)):
    """Retorna os dados de um usuário."""
    return await use.get_user_by_id(token["id"])
