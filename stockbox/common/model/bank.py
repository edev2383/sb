from sqlalchemy import Column, Integer, String, Float
from .base import Base


class Bank(Base):
    """Model Bank

    Args:
        Base ([type]): [description]
    """

    __tablename__ = "Bank"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    initial_deposit = Column(Float)
