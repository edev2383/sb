"""  ooo """
from sqlalchemy import Column, Integer, String, Float
from .base import Base

class StockWeeklyData(Base):
    """ ooo """
    __tablename__ = "StockWeeklyData"
    id  = Column(Integer, primary_key=True)
    stock_id = Column(Integer)
    high = Column(Float)
    low = Column(Float)
    open = Column(Float)
    close = Column(Float)
    volume = Column(Integer)
    date = Column(String)
    timestamp= Column(Integer)
