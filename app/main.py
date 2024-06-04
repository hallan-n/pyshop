from infra.connection import Connection

conn = Connection()


async def rodar():
    async with conn as cn:
        ...


import asyncio

loop = asyncio.get_event_loop()
loop.run_until_complete(rodar())
