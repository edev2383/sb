from stockbox.database import session
from stockbox.model import Stock
from stockbox.ticker import Ticker

result = session.query(Stock).all()

for row in result:
    Ticker(row.symbol)
