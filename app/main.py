import uvicorn
from fastapi import FastAPI
from infra.routes.user_route import route

app = FastAPI()
app.include_router(route)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
