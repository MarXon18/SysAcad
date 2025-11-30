from marshmallow import Schema, fields, validate, post_load
from app.models import Cargo
from app.mapping.categoriacargo_mapping import CategoriaCargoMapping
from app.mapping.tipodedicacion_mapping import TipoDedicacionMapping
from app.repositories import CategoriaCargoRepository, TipoDedicacionRepository

class CargoMapping(Schema):
    hashid = fields.Int()
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    puntos = fields.Integer(allow_none=True)

    @post_load
    def nuevo_cargo(self, data, **kwargs):
        return Cargo(**data)