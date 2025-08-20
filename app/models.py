
from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class Restaurant(SQLModel, table=True):
    id: int = Field(primary_key=True,)
    name: str = Field(index=True)
