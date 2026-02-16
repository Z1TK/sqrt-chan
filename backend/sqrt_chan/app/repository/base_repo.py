from sqlalchemy import and_, delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from backend.sqrt_chan.app.models.base import Base
from backend.sqrt_chan.app.utils.decorators import handler_db_errors


class BaseRepository[T: Base]:
    def __init__(self, model: type[T], async_session: AsyncSession):
        self.model = model
        self.session = async_session

    # @handler_db_errors
    # async def get_all(self, model_slug: str | None = None, model_id: int | None = None) -> list[T]:
    #     conditions = []
    #     if model_slug:
    #         conditions.append(self.model.slug == model_slug)
    #     if model_id:
    #         conditions.append(self.model.id == model_id)
    #     stmt = select(self.model).where(and_(*conditions)) if conditions else select(self.model)
    #     res = await self.session.execute(stmt)
    #     return res.scalars().all()

    @handler_db_errors
    async def create(self, **kwargs) -> T:
        obj = self.model(**kwargs)
        self.session.add(obj)
        await self.session.flush()
        await self.session.refresh(obj)
        return obj

    # @handler_db_errors
    # async def update(
    #     self, model_slug: str | None = None, model_id: int | None = None, **kwargs
    # ):
    #     condition = []
    #     if model_id is not None:
    #         condition.append(self.model.id == model_id)
    #     if model_slug is not None:
    #         condition.append(self.model.slug == model_slug)
    #     stmt = (
    #         update(self.model)
    #         .where(and_(*condition))
    #         .values(**kwargs)
    #         .returning(self.model)
    #     )
    #     res = await self.session.execute(stmt)
    #     await self.session.flush()
    #     return res.scalar_one_or_none()

    # @handler_db_errors
    # async def remove(
    #     self, model_slug: str | None = None, model_ids: list[int] | None = None
    # ) -> None:
    #     conditions = []
    #     if model_slug is not None:
    #         conditions.append(self.model.slug == model_slug)
    #     if model_ids is not None:
    #         conditions.append(self.model.id.in_(model_ids))
    #     stmt = delete(self.model).where(and_(*conditions))
    #     await self.session.execute(stmt)
    #     await self.session.flush()
