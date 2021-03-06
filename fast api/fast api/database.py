from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql://root:password@mysqldb/family"
#SQLALCHEMY_DATABASE_URL = "sqlite:///./family"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
try:
    engine = create_engine(
            SQLALCHEMY_DATABASE_URL, pool_size=15 
            )
except e:
    print("error connection failed!! ", e)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
