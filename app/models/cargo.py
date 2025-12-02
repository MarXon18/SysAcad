from dataclasses import dataclass
from app import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String

@dataclass(init=False, repr=True, eq=True)
class Cargo(db.Model):  # Ahora Cargo hereda de db.Model
    __tablename__ = 'cargos'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    puntos: Mapped[int] = mapped_column(Integer, nullable=False)

    categoria_cargo_id: Mapped[int] = mapped_column(Integer, db.ForeignKey('categoria_cargos.id'), nullable=True)
    tipo_dedicacion_id: Mapped[int] = mapped_column(Integer, db.ForeignKey('tipo_dedicaciones.id'), nullable=True)
