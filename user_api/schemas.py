"""
    Pydantic schema definition
"""
from pydantic import BaseModel


class User(BaseModel):
    """User schema definition"""

    name: str

    class Config:
        """Custom config for this schema"""

        orm_mode = True
