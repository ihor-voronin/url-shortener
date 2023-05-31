import os
from typing import Any

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.exc import DBAPIError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///app.db")
engine = create_engine(DATABASE_URL)
Base: Any = declarative_base()
DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_session():
    session = DBSession()
    try:
        yield session
    except DBAPIError:
        session.rollback()
    finally:
        session.close()


class ShortUrl(Base):
    __tablename__ = "short_urls"

    id = Column(Integer, primary_key=True)
    original_url = Column(String(255))
    short_url = Column(String(7), unique=True, index=True)
