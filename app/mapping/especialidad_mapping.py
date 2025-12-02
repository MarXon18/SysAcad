from marshmallow import Schema, fields, post_load, validate
from app.models import Especialidad

class EspecialidadMapping(Schema):
    id= fields.Integer(dump_only=True)
    nombre= fields.String(required=True, validate=validate.Length(min=1, max=100))
    letra= fields.String(required=True, validate=validate.Length(min=1, max=100))
    observacion= fields.String(required=True, validate=validate.Length(min=1, max=100))
    tipo_especialidad_id= fields.Int(allow_none= True)

    @post_load
    def nueva_especialidad(self, data, **kwargs):
        return Especialidad(**data)