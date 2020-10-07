"""  ooo """
from sqlalchemy import Column, Integer, Float
from .base import Base


class StockIndicatorData(Base):
    """ ooo """

    __tablename__ = "StockIndicatorData"
    id = Column(Integer, primary_key=True)
    stock_indicator_id = Column(Integer)
    stock_data_id = Column(Integer)
    value = Column(Float)
