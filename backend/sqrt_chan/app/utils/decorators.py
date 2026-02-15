from functools import wraps

from sqlalchemy.exc import DataError, IntegrityError, NoResultFound, OperationalError


def handler_db_errors(func):
    @wraps(func)
    async def wrapper(self, *arg, **kwargs):
        try:
            return await func(self, *arg, **kwargs)
        except IntegrityError as e:
            await self.session.rollback()
            print(e)
            raise
        except OperationalError as e:
            await self.session.rollback()
            print(e)
            raise
        except DataError as e:
            await self.session.rollback()
            print(e)
            raise
        except NoResultFound as e:
            await self.session.rollback()
            print(e)
            raise

    return wrapper
