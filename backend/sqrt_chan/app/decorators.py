from functools import wraps

from sqlalchemy.exc import (DataError, IntegrityError, NoResultFound,
                            OperationalError)


def handler_db_errors(func):
    @wraps(func)
    async def wrapper(self, *arg, **kwargs):
        try:
            return await func(self, *arg, **kwargs)
        except IntegrityError as e:
            self.session.rollback()
            print(e)
            raise
        except OperationalError as e:
            self.session.rollback()
            print(e)
            raise
        except DataError as e:
            self.session.rollback()
            print(e)
            raise
        except NoResultFound as e:
            self.session.rollback()
            print(e)
            raise
