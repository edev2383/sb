"""  ooo """
from sqlalchemy import Column, Integer, Float
from .base import Base


class StockWeeklyIndicatorData(Base):
    """ ooo """

    __tablename__ = "StockWeeklyIndicatorData"
    id = Column(Integer, primary_key=True)
    stock_weekly_indicator_id = Column(Integer)
    stock_weekly_data_id = Column(Integer)
    value = Column(Float)
