from database.models import user
from database.common.base import session_factory, engine, Base


class DataBaseInstance(object):
    def __new__(cls):
        db = session_factory()
        try:
            yield db
        finally:
            db.close()
        return db


def create_tables():
    user.Base.metadata.create_all(engine, Base.metadata.tables.values(), checkfirst=True)


if __name__ == '__main__':
    database = DataBaseInstance()
    create_tables()
