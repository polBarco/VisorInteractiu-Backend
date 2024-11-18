import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

database_url = os.getenv("DATABASE_URL")

if database_url is None:
    # Si DATABASE_URL no está definida, usar variables específicas para entorno local
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")

    if (user is None) or (password is None) or (host is None) or (port is None) or (database is None):
        print(f"user: {user}, password: {password}, host: {host}, port: {port}, database: {database}")
        raise Exception("Database credentials not found in .env file")

    # Construir la URL de la base de datos con los valores obtenidos de las variables de entorno locales
    database_url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

# user = os.getenv("DB_USER")
# password = os.getenv("DB_PASSWORD")
# host = os.getenv("DB_HOST")
# port = os.getenv("DB_PORT")
# database = os.getenv("DB_NAME")

# if (user is None) or (password is None) or (host is None) or (port is None) or (database is None):
#     print(f"user: {user}, password: {password}, host: {host}, port: {port}, database: {database}")

#     raise Exception("Database credentials not found in .env file")

# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://"+user+":"+password+"@"+host+":"+port+"/"+database

# engine = create_engine(SQLALCHEMY_DATABASE_URL)
engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()