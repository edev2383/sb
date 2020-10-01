from sqlalchemy import Column, Integer, String, Float
from .base import Base


class StockData(Base):
    """ ooo """

    __tablename__ = "StockData"

    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer)
    High = Column(Float)
    Low = Column(Float)
    Open = Column(Float)
    Close = Column(Float)
    Volume = Column(Integer)
    Date = Column(String)
