import uvicorn
from fastapi import FastAPI
from infra.routes.auth import route as auth
from infra.routes.user_route import route as user

app = FastAPI()
app.include_router(user)
app.include_router(auth)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
