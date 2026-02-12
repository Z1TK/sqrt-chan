from typing import Callable

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.sqrt_chan.app.database.db import async_session


async def get_async_session():
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        finally:
            await session.close()


def get_service[S, R](service: type[S], repo: type[R]) -> Callable[[AsyncSession], S]:
    def _get_service(session: AsyncSession = Depends(get_async_session)) -> S:
        return service(repo(session))

    return _get_service
