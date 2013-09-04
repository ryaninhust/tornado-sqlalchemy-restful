from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Put your models here
class TestModel(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    name = Column(String(1000))

    def __repr(self):
        return '<Test: %d>' % self.id


def init_db(engine):
    Base.metadata.create_all(bind=engine)
