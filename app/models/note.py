from sqlalchemy.orm import Mapped,mapped_column
from app.db import Base

class Note(Base):
    
    __tablename__ = "Note"
    
    id : Mapped[int] = mapped_column(nullable=False,primary_key=True , autoincrement=True)
    body : Mapped[str] = mapped_column(nullable=True)