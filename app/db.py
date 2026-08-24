from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL ="sqlite:///./sandbox.db"

engine = create_engine(DATABASE_URL,connect_args={"check_same_thread": False})
sessionlocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

