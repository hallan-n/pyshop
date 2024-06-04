from infra.repositories import Repositories
from infra.schemas import user_table

repo = Repositories()
async def rodar():
    data = await repo.execute_sql("SELECT * FROM user;")
    print(data)


import asyncio

loop = asyncio.get_event_loop()
loop.run_until_complete(rodar())
