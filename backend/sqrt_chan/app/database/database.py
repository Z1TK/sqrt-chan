from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from backend.sqrt_chan.core.config import setting

db_url = setting.get_db_url()

engine = create_async_engine(db_url, echo=True)

async_session = async_sessionmaker(engine, expire_on_commit=False)