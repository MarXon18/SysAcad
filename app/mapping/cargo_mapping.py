from marshmallow import Schema, fields, validate, post_load
from app.models import Cargo
from app.mapping.categoriacargo_mapping import CategoriaCargoMapping
from app.mapping.tipodedicacion_mapping import TipoDedicacionMapping
from app.repositories import CategoriaCargoRepository, TipoDedicacionRepository

class CargoMapping(Schema):
    hashid = fields.String(dump_only=True)
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    puntos = fields.Integer(allow_none=True)
    categoria_cargo_id = fields.Integer(allow_none=True)
    tipo_dedicacion_id = fields.Integer(allow_none=True)

    @post_load
    def nuevo_cargo(self, data, **kwargs):
        return Cargo(**data)