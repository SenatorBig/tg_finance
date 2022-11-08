from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    chat_id = Column(String, unique=True)
    currency = Column(String)
    balance = Column(Float)
    is_active = Column(Boolean, default=True)
    purchase = relationship("Purchase")


class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    price = Column(Float)
    created_at = Column(DateTime)
    store_id = Column(Integer, ForeignKey("stores.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))


class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    purchase = relationship("Purchase")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    purchase = relationship("Purchase")
