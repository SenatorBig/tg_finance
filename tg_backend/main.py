from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from settings import DB_URL

Base = declarative_base()
engine = create_engine(DB_URL)




# приложение, которое ничего не делает
app = FastAPI()

