from marshmallow import fields, Schema, post_load, validate
from app.models import Orientacion

class OrientacionMapping(Schema):
    id= fields.Integer(dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    materia = fields.Int(allow_none=True)
    especialidad_id = fields.Int(allow_none=True)
    plan_id= fields.Int(allow_none=True)

    @post_load
    def nueva_orientacion(self, data, **kwargs):
        return Orientacion(**data)