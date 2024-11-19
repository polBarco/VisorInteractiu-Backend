import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Si no existe `DATABASE_URL`, significa que estás en desarrollo local y necesitas las variables separadas.
if SQLALCHEMY_DATABASE_URL is None:
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")

    if (user is None) or (password is None) or (host is None) or (port is None) or (database is None):
        print(f"user: {user}, password: {password}, host: {host}, port: {port}, database: {database}")
        raise Exception("Database credentials not found in .env file")

    SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# user = os.getenv("DB_USER")
# password = os.getenv("DB_PASSWORD")
# host = os.getenv("DB_HOST")
# port = os.getenv("DB_PORT")
# database = os.getenv("DB_NAME")

# if (user is None) or (password is None) or (host is None) or (port is None) or (database is None):
#     print(f"user: {user}, password: {password}, host: {host}, port: {port}, database: {database}")

#     raise Exception("Database credentials not found in .env file")

# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://"+user+":"+password+"@"+host+":"+port+"/"+database