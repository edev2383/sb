"""  ooo """
from sqlalchemy import Column, Integer, String
from .base import Base

class StockWeeklyIndicator(Base):
    """ ooo """
    __tablename__ = "StockWeeklyData"
    id  = Column(Integer, primary_key=True)
    name = Column(String)
    range_one = Column(Integer)
    range_two = Column(Integer)
