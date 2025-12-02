from dataclasses import dataclass  
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from app import db

@dataclass(init=False, repr=True, eq=True)
class Nota(db.Model):
    __tablename__ = 'notas'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    calificacion: Mapped[str] = mapped_column(String(10), nullable=False)
