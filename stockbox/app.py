from .database.conn import session
from .model.stock import Stock
 
def run():
    s1 = Stock(symbol="MSFT")
    session.add(s1)
    session.commit()
