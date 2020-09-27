"""  ooo """
from sqlalchemy import Column, Integer, String
from .base import Base

class Stock(Base):
    """ ooo """
    __tablename__ = "Stock"
    id  = Column(Integer, primary_key=True)
    symbol = Column(String)
