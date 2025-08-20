
from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class Restaurant(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True,)
    name: str = Field(index=True)
    description: str | None = Field(default=None, nullable=True)
    price: int | None = Field(default=None, nullable=True)
    address: str | None = Field(default=None, nullable=True)

class Tag(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True,)
    name: str = Field(index=True)