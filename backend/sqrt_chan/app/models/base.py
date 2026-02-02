from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs

class Base(DeclarativeBase, AsyncAttrs):
    __abstruct__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + 's'