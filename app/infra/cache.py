import json
from os import getenv

import redis


class Cache:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.redis = redis.Redis(
                host=getenv("REDIS_HOST"),
                port=int(getenv("REDIS_PORT")),
                db=int(getenv("REDIS_DB")),
                decode_responses=True,
            )
            cls._instance.expire = int(getenv("REDIS_EXPIRE_MINUTES")) * 60
        return cls._instance

    @classmethod
    def set(cls, key, data):
        try:
            cls.instance().redis.setex(
                f"{key}:{data}", cls.instance().expire, json.dumps(data)
            )
        except redis.RedisError as e:
            raise Exception(f"Erro ao definir chave no Redis: {e}")


    @classmethod
    def has(cls, key, value):
        try:
            return bool(cls.instance().redis.exists(f"{key}:{value}"))
        except redis.RedisError as e:
            raise Exception(f"Erro ao verificar existência de chave no Redis: {e}")

    @classmethod
    def clear(cls):
        try:
            cls.instance().redis.flushdb()
        except redis.RedisError as e:
            raise Exception(f"Erro ao limpar o banco de dados Redis: {e}")

    @classmethod
    def exists(cls, key):
        return bool(cls.instance().redis.exists(key))

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
