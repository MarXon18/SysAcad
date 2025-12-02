from dataclasses import dataclass  
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from app import db

@dataclass(init=False, repr=True, eq=True)
class TipoEspecialidad(db.Model):
    __tablename__ = 'tipo_especialidades'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    nivel: Mapped[str] = mapped_column(String(2), nullable=False)
