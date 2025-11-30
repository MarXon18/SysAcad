from marshmallow import Schema, fields, validate, post_load
from app.models import Departamento

class DepartamentoMapping(Schema):
    hashid = fields.Int(dump_only=True)
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    orientacion_id = fields.Integer(allow_none=True)

    @post_load
    def nuevo_departamento(self, data, **kwargs):
        return Departamento(**data)