from dataclasses import dataclass  
from app import db
from app.models.facultad import Facultad
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey

@dataclass(init=False, repr=True, eq=True)
class Universidad(db.Model):  
    __tablename__ = 'universidades'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    sigla: Mapped[str] = mapped_column(String(5), nullable=False)

    facultad_id: Mapped[int] = mapped_column(ForeignKey('facultades.id'), nullable=True)
    facultad: Mapped["Facultad"] = relationship('Facultad', backref='universidades')
