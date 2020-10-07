"""  ooo """
from sqlalchemy import Column, Integer, String
from .base import Base


class StockIndicator(Base):
    """ ooo """

    __tablename__ = "StockIndicator"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    range_one = Column(Integer)
    range_two = Column(Integer)
