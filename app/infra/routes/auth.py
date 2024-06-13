from domain.usecases.user_usecase import UserUseCase
from fastapi import APIRouter, Header
from infra.security import Security

from domain.models.user import UserLogin

use = UserUseCase()
security = Security()

route = APIRouter(tags=["Auth"], prefix="/auth")


@route.post("/login")
async def get_auth(user: UserLogin):
    user_auth = await use.get_user_by_login(user)
    data = {"sub": user_auth.email, "id": user_auth.id}
    access_token = security.create_access_token(data=data)
    return {"access_token": access_token, "token_type": "bearer"}


@route.post("/logout")
async def revoke_auth(token: str = Header(...)):
    security.revoke_access_token(token)
