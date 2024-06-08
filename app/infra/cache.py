import json
from os import getenv

import redis


class Cache:
    def __init__(self):
        self.redis = redis.Redis(
            host=getenv("REDIS_HOST"),
            port=int(getenv("REDIS_PORT")),
            db=int(getenv("REDIS_DB")),
            decode_responses=True,
        )
        self.expire = int(getenv("REDIS_EXPIRE_MINUTES")) * 60

    def set(self, key, data):
        self.redis.setex(f"{key}:{data}", self.expire, json.dumps(data))

    def has(self, key, value):
        return bool(self.redis.exists(f"{key}:{value}"))

    def clear(self):
        self.redis.flushdb()

    def exists(self, key):
        return bool(self.redis.exists(key))
