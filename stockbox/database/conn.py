""" testing something here """
import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

env_path = Path("../../../..") / ".env"
load_dotenv(dotenv_path=env_path)

prefix: str = "mysql+pymysql"
user: str = os.getenv("DB_USER")
pw: str = os.getenv("DB_PASS")
host: str = os.getenv("DB_HOST")
db_name: str = os.getenv("DB_NAME")

dns: str = f"{prefix}://{user}:{pw}@{host}/{db_name}"

engine = create_engine(dns, echo=False)

Session = sessionmaker(bind = engine)
session = Session()

