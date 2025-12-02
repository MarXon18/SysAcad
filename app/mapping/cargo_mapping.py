from marshmallow import Schema, fields, validate, post_load
from app.models import Cargo
from app.mapping.categoriacargo_mapping import CategoriaCargoMapping
from app.mapping.tipodedicacion_mapping import TipoDedicacionMapping
from app.repositories import CategoriaCargoRepository, TipoDedicacionRepository

class CargoMapping(Schema):
    hashids = fields.String(attribute="hashid", dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=50))
    puntos = fields.Integer(required=True, validate=validate.Range(min=0))
    categoria_cargo_id = fields.Integer(required=True, load_only=True)
    categoria= fields.Nested('CategoriaCargoMapping', only=('hashids', 'nombre'), dump_only=True)
    tipo_dedicacion_id = fields.Integer(allow_none=True)

    @post_load
    def nuevo_cargo(self, data, **kwargs) -> Cargo:
        return Cargo(**data)