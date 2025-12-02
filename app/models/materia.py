from dataclasses import dataclass  
from app.models.nota import Nota
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from app import db

@dataclass(init=False, repr=True, eq=True)
class Materia(db.Model):
    __tablename__ = 'materias'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    codigo: Mapped[str] = mapped_column(String(100), nullable=False)
    observacion: Mapped[str] = mapped_column(String(100), nullable=False)

    nota_id: Mapped[int] = mapped_column(ForeignKey('notas.id'), nullable=True)
    nota: Mapped["Nota"] = relationship('Nota', backref='materias')

