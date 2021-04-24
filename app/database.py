from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import dotenv_values, find_dotenv

config = dotenv_values(find_dotenv())
username = os.environ.get("USERNAME_DB") or config["USERNAME_DB"]
password = os.environ.get("PASSWORD_DB") or config["PASSWORD_DB"]
database = os.environ.get("DATABASE") or config["DATABASE"]
host = os.environ.get("HOST") or config["HOST"]
print(username,password,database,host)
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://"+username+":"+password+"@"+host+"/"+database


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()