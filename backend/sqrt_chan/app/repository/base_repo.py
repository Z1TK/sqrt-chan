from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update, delete, select
from backend.sqrt_chan.app.models.base import Base
from backend.sqrt_chan.app.decorators import handler_db_errors

class BaseRepository[T: Base]:
    def __init__(self, model: type[T], async_session: AsyncSession):
        self.model = model
        self.session = async_session

    @handler_db_errors
    async def get_all(self) -> list[T]:
        stmt = select(self.model)
        res = await self.session.execute(stmt)
        return res.scalar.all()

    @handler_db_errors
    async def create(self, **kwargs) -> T:
        obj = self.model(**kwargs)
        self.session.add()
        await self.session.commit()
        await self.session.refresh(obj)
        return obj
    
    @handler_db_errors
    async def update(self, model_id: int, **kwargs) -> T | None:
        stmt = update(self.model).filter_by(id=model_id).values(**kwargs).returning(self.model)
        res = await self.session.execute(stmt)
        await self.session.commit()
        return res.scalar_one_or_none()
    
    @handler_db_errors
    async def remove(self, model_id: int) -> None:
        stmt = delete(self.model).filter_by(id=model_id)
        await self.session.execute(stmt)
        await self.session.commit()
