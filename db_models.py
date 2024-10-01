from sqlalchemy import Column, Integer, Boolean, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Weapon(Base):
    __tablename__ = 'weapons'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    category = Column(String)
    reinforcement = Column(String)
