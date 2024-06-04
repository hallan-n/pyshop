from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.infra.schemas import metadata


class Connection:
    _tables_created = False

    def __init__(self) -> None:
        self.url = "mysql+aiomysql://root:123456@localhost:3306/pyshop"
        self.engine = create_async_engine(
            self.url, echo=True, pool_size=10, max_overflow=20
        )
        self.session_maker = sessionmaker(
            bind=self.engine, class_=AsyncSession, expire_on_commit=False
        )

    async def _create_tables(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(metadata.create_all)
        self._tables_created = True

    async def __aenter__(self):
        if not self._tables_created:
            print("criou")
            await self._create_tables()
        self.session = self.session_maker()
        return self.session

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.session.commit()
        await self.session.close()
