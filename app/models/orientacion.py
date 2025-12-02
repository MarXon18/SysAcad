from dataclasses import dataclass  
from app.models.plan import Plan
from app.models.materia import Materia
from app.models.especialidad import Especialidad
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from app import db

@dataclass(init=False, repr=True, eq=True)
class Orientacion(db.Model):
    __tablename__ = 'orientaciones'
    __allow_unmapped__ = True 
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)

    plan_id: Mapped[int] = mapped_column(ForeignKey('planes.id'), nullable=True)
    plan: Mapped["Plan"] = relationship('Plan', backref='orientaciones')

    materia_id: Mapped[int] = mapped_column(ForeignKey('materias.id'), nullable=True)
    materia: Mapped["Materia"] = relationship('Materia', backref='orientaciones')

    especialidad_id: Mapped[int] = mapped_column(ForeignKey('especialidades.id'), nullable=True)
    especialidad: Mapped["Especialidad"] = relationship('Especialidad', backref='orientaciones')    
