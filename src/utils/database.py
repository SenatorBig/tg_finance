from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from data.config import DB_URL
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine(DB_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    chat_id = Column(String, unique=True)
    currency = Column(String)
    balance = Column(Float)
    is_active = Column(Boolean, default=True)
    purchase = relationship("Purchase", cascade="all, delete, delete-orphan")
    category = relationship("Category", cascade="all, delete, delete-orphan")
    store = relationship("Store", cascade="all, delete, delete-orphan")


class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    price = Column(Float)
    created_at = Column(DateTime, default=datetime.now)
    store_id = Column(Integer, ForeignKey("stores.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))


class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    purchase = relationship("Purchase")
    user_id = Column(Integer, ForeignKey("users.id"))


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    purchase = relationship("Purchase")
    user_id = Column(Integer, ForeignKey("users.id"))

