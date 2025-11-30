from marshmallow import Schema, fields, validate, post_load
from app.models import CategoriaCargo

class CategoriaCargoMapping(Schema):
    hashid = fields.String(dump_only = True)
    nombre = fields.String(required = True, validate = validate.Length(min = 1, max = 50))

    @post_load
    def make_categoria_cargo(self, data, **kwargs):
        return CategoriaCargo(**data)

