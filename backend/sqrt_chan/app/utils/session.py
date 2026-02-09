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
            session.close()


def get_repository[T](repo: type[T]) -> Callable[[AsyncSession], T]:
    def _get_repo(session: AsyncSession = Depends(get_async_session)) -> T:
        return repo(session)

    return _get_repo
