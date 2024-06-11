from datetime import datetime, timedelta
from os import getenv

import bcrypt
from fastapi import Header, HTTPException, status
from infra.cache import Cache
from jose import JWTError, jwt


class Security:
    def __init__(self) -> None:
        self._SECRET_KEY = getenv("SECRET_KEY")
        self._ALGORITHM = getenv("ALGORITHM")
        self._EXPIRE = int(getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
        self.cache = Cache()

    def hashed(self, password: str):
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hash.decode("utf-8")

    def check_hash(self, hashed: str, password: str):
        return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))

    def create_access_token(self, data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=self._EXPIRE)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self._SECRET_KEY, algorithm=self._ALGORITHM)
        return encoded_jwt

    def revoke_access_token(self, token: str):
        self.cache.set("blacklist", token)

    def decode_token(self, token: str = Header(...)):
        try:
            if self.cache.has("blacklist", token):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token incorreto ou expirado.",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            payload = jwt.decode(token, self._SECRET_KEY, algorithms=[self._ALGORITHM])
            return payload
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token incorreto ou expirado.",
                headers={"WWW-Authenticate": "Bearer"},
            )
