"""Database properties configuration
"""
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///user.db")
connection_args = {}
if "sqlite" in DATABASE_URL:
    connection_args["check_same_thread"] = False
engine = create_engine(DATABASE_URL, connect_args=connection_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
