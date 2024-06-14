import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from infra.routes.auth import route as auth
from infra.routes.product_router import route as product
from infra.routes.user_route import route as user

load_dotenv()
app = FastAPI()

app.include_router(user)
app.include_router(auth)
app.include_router(product)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
