import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

db_host = os.getenv('DB_HOST')
db_host_test = os.getenv('DB_HOST_TEST')

connection_db_url = os.getenv('DB_URL_TEST') if db_host_test else os.getenv('DB_URL')

engine = create_engine(connection_db_url, echo=False)

Session = sessionmaker(bind=engine)
session = Session()
