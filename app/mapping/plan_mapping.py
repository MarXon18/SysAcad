from marshmallow import Schema, fields, validate, post_load
from app.models import Plan

class PlanMapping(Schema):
    hashid = fields.String(dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    fecha_inicio = fields.DateTime(required=True)
    fecha_fin = fields.DateTime(required=True)
    observacion = fields.String(required=True, validate=validate.Length(min=1, max=500))

    @post_load
    def nuevo_plan(self, data, **kwargs):
        return Plan(**data)