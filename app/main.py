from domain.usecases.user_usecase import UserUseCase
from domain.models import User
from fastapi import FastAPI
import uvicorn

use = UserUseCase()
app = FastAPI()

@app.post('/')
async def main(user: User):
    await use.create_user(user)

if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)