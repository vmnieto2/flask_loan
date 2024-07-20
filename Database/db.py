import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import NullPool
import os
from dotenv import load_dotenv


BASE = declarative_base() 
load_dotenv()

user = os.getenv("DB_USER")
passwd = os.getenv("DB_PASS")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

connect_url = sqlalchemy.engine.url.URL(
    "mysql+pymysql",
    username=user,
    password=passwd,
    host=host,
    port=int(port),
    database=db_name,
    query=dict(charset="utf8mb4")
)

engine = sqlalchemy.create_engine(connect_url, poolclass=NullPool)

session_maker = sessionmaker(bind=engine)

session = session_maker()
        