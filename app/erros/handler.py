from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError


class HandlerErrors:
    def __init__(self, app: FastAPI) -> None:
        self.app = app

    @classmethod
    async def erro_entity(request: Request, exc: RequestValidationError):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Deu ruim paezão')