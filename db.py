from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# dotenv

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

# adapt dotenv to postgresql url
 
url_object = URL.create(
    "postgresql+psycopg",
    username=db_user,
    password=db_password,
    host=db_host,
    port=db_port,
    database=db_name
)

# create engine with url

engine = create_engine(url_object, pool_pre_ping=True)

# declarate session local

SessionLocal = sessionmaker(engine)

# get database def to make changes or consult

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()