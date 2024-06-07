from domain.models import User
from domain.usecases.user_usecase import UserUseCase
from fastapi import APIRouter
from infra.security import Security

use = UserUseCase()
security = Security()

route = APIRouter(tags=["Auth"], prefix="/auth")


@route.post("/")
async def get_auth(user: User):
    user_auth = await use.get_user_by_login(user)
    data = {"sub": user_auth.email}
    access_token = security.create_access_token(data=data)
    return {"access_token": access_token, "token_type": "bearer"}
