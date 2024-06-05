from infra.connection import Connection
from sqlalchemy import select, insert, update, delete, text


class Repositories:
    def __init__(self):
        self.conn = Connection()

    async def create(self, schema, data):
        async with self.conn as conn:
            try:
                stmt = insert(schema).values(**data)
                await conn.execute(stmt)
                return True
            except:
                return False

    async def update(self, schema, data):
        async with self.conn as conn:
            try:
                stmt = update(schema).where(schema.c.id == data["id"]).values(**data)
                await conn.execute(stmt)
                return True
            except:
                return False

    async def read(self, schema, id):
        async with self.conn as conn:
            try:
                stmt = select(schema).where(schema.c.id == id)
                result = await conn.execute(stmt)
                return result.mappings().fetchone()
            except:
                return False

    async def read_all(self, schema):
        async with self.conn as conn:
            try:
                stmt = select(schema)
                result = await conn.execute(stmt)
                return result.mappings().fetchall()
            except:
                return False

    async def delete(self, schema, id):
        async with self.conn as conn:
            try:
                stmt = delete(schema).where(schema.c.id == id)
                await conn.execute(stmt)
                return True
            except:
                return False

    async def execute_sql(self, query):
        async with self.conn as conn:
            try:
                result = await conn.execute(text(query))
                try:
                    return result.mappings().fetchall()
                except:
                    return True
            except:
                return False
