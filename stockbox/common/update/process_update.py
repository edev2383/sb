from stockbox.database import session
from stockbox.model import Stock
from stockbox.ticker import Ticker
import logging

s = Stock(symbol="TEST")

session.add(s)
session.commit()

logging.basicConfig(
    filename="/var/www/edickdev/cgi-bin/py/sb/app.log",
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s",
)
logging.warning("Testing cron job - ran session")
