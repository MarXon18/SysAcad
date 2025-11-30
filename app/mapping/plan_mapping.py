from marshmallow import Schema, fields, validate, post_load
from app.models import Plan

class PlanMapping(Schema):
    hashid = fields.String(dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    fecha_inicio = fields.Date(required=True)
    fecha_fin = fields.Date(required=True)
    observacion = fields.String(validate=validate.Length(max=255))

    @post_load
    def nuevo_plan(self, data, **kwargs):
        return Plan(**data)