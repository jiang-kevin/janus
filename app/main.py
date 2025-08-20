from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI, Depends
from sqlmodel import Session

from database import Database
from models import Restaurant


db = Database()

@asynccontextmanager
async def lifespan(app: FastAPI):
    db.create()
    yield

app = FastAPI(lifespan=lifespan, root_path="/api/v1")
SessionDep = Annotated[Session, Depends(db.session)]


@app.get("/restaurants")
async def get_restaurants(session: SessionDep):
    return session.query(Restaurant).all()

@app.get("/restaurants/{name}")
async def get_restaurant_by_id(name: str, session: SessionDep):
    return session.get(Restaurant, name)

@app.post("/restaurants")
async def create_restaurant(restaurant: Restaurant, session: SessionDep):
    session.add(restaurant)
    session.commit()