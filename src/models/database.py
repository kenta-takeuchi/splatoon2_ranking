from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class BaseEngine(object):
    def __init__(self):
        self.engine = create_engine('sqlite:///db.sqlite3', echo=True)


class BaseSession(BaseEngine):
    def __init__(self):
        super().__init__()
        session = sessionmaker(bind=self.engine)
        self.session = session()
