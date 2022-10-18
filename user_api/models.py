"""
    SQLAlchemy schema definition
"""
from sqlalchemy import Column, Integer, String

from .database import Base


class User(Base):
    """User schema

    Args:
        Base : sqlachemy declarative base
    """

    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256))
