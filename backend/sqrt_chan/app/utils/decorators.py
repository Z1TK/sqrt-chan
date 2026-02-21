from functools import wraps
import logging

from sqlalchemy.exc import (DataError, IntegrityError, NoResultFound,
                            OperationalError)
from backend.sqrt_chan.app.logger import log

def handler_db_errors(func):
    @wraps(func)
    async def wrapper(self, *arg, **kwargs):
        try:
            return await func(self, *arg, **kwargs)
        except IntegrityError as e:
            await self.session.rollback()
            log.error('IntegrityError in %s: %s', func.__name__, e)
            raise
        except OperationalError as e:
            await self.session.rollback()
            log.error('OperationalError in %s: %s', func.__name__, e)
            raise
        except DataError as e:
            await self.session.rollback()
            log.error('DataError in %s: %s', func.__name__, e)
            raise
        except NoResultFound as e:
            await self.session.rollback()
            log.error('NoResultFound in %s: %s', func.__name__, e)
            raise

    return wrapper
