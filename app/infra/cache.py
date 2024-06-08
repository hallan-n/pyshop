import json
from os import getenv

import redis


class Cache:
    def __init__(self):
        self.redis = redis.Redis(
            host=getenv("REDIS_HOST"),
            port=int(getenv("REDIS_PORT")),
            db=int(getenv("REDIS_DB")),
        )
        self.expire = int(getenv("REDIS_EXPIRE_MINUTES")) * 60

    def set(self, key, data):
        if self.redis.exists(key):
            self.redis.delete(key)
        self.redis.setex(key, self.expire, json.dumps(data))

    def get(self, key):
        if self.redis.exists(key):
            return json.loads(self.redis.get(key))
        return None

    def clear(self):
        self.redis.flushdb()

    def exists(self, key):
        return bool(self.redis.exists(key))
