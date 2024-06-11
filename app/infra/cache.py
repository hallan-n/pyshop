import json
from os import getenv

import aioredis


class Cache:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Cache, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self) -> None:
        if self._initialized:
            return
        self.redis_host = getenv("REDIS_HOST", "localhost")
        self.redis_port = int(getenv("REDIS_PORT", 6379))
        self.redis_db = int(getenv("REDIS_DB", 0))
        self.expire = int(getenv("REDIS_EXPIRE_MINUTES", 5)) * 60
        self._initialized = True

    async def initialize(self):
        self.redis = await aioredis.create_redis_pool(
            (self.redis_host, self.redis_port),
            db=self.redis_db,
            decode_responses=True,
        )

    async def set(self, key, data):
        await self.redis.setex(f"{key}:{data}", self.expire, json.dumps(data))

    async def has(self, key, value):
        return bool(await self.redis.exists(f"{key}:{value}"))

    async def clear(self):
        await self.redis.flushdb()

    async def exists(self, key):
        return bool(await self.redis.exists(key))

    async def close(self):
        self.redis.close()
        await self.redis.wait_closed()

    async def __aenter__(self):
        await self.initialize()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.close()
