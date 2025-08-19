from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import Database
from models import Restaurant


db = Database()

@asynccontextmanager
async def lifespan(app: FastAPI):
    db.create()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/restaurants/{name}")
async def get_restaurant(name: str):
    return db.session()
