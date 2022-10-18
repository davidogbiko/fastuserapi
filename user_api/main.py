"""
    This is a base application for fetching and saving user names in python using FASTAPI
"""
import csv
from io import StringIO

from fastapi import Depends, FastAPI, File, UploadFile, status
from fastapi.openapi.utils import get_openapi
from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db_conn():
    """Establish database connection."""
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def custom_openapi():
    """Customise generated openapi fields

    Returns:
        custom openapi_schema
    """
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="User API",
        description="A Very Simple User API",
        version="1.0.0",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@app.get("/")
def root() -> dict[str, str]:
    """Root path

    Returns:
        dict[str, str]: Message from the root path to verify server functionality (healthcheck)
    """
    return {"message": "Welcome to User API"}


@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db_conn)):
    """Fetch details for a single user in the database

    Args:
        db (Session): database session
        user_id (int): User ID

    Returns:
        user: User details with the given ID
    """
    return db.query(models.User).filter(models.User.id == user_id).first()


@app.get("/users")
def get_users(db: Session = Depends(get_db_conn)) -> list:
    """Fetch users in the database with optionally specified offsets and limits

    Args:
        db (Session): Database session
        skip (int, optional): Position to start user data read. Defaults to 0.
        limit (int, optional): Position to stop read. Defaults to 100.

    Returns:
        Users: List of Users matching the predefined offsets and limits
    """
    return db.query(models.User).all()


@app.post("/users/", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.User, db: Session = Depends(get_db_conn)):
    """Create new user and add them to database

    Args:
        db (Session): Database session
        user (schemas.UserCreate): User schema

    Returns:
        user : User object stored in the database
    """
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.post("/users/upload", status_code=status.HTTP_201_CREATED)
async def create_users(
    file: UploadFile = File(...), db: Session = Depends(get_db_conn)
) -> dict[str, str]:
    """Create multiple users from csv file

    Args:
        db (Session): Database session
        user (schemas.UserCreate): User schema

    Returns:
        user : User object stored in the database
    """
    # data = {}
    file_contents = file.file.read()
    buffer = StringIO(file_contents.decode("utf-8"))
    new_users = csv.DictReader(buffer)
    for user in new_users:
        db_user = models.User(name=user["name"])
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    buffer.close()
    file.file.close()
    return {"message": "Users created successfully!"}
