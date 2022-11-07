from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()
engine = create_engine('postgresql://releven:releven@{}:5432/database'.format('tg_finance_postgres_1'))




# приложение, которое ничего не делает
app = FastAPI()

