from marshmallow import Schema, fields, post_load, validate
from app.models import TipoDedicacion

class TipoDedicacionMapping(Schema):
    hashid = fields.String(dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    observacion = fields.String(validate=validate.Length(min=1, max=255))

    @post_load
    def nuevo_tipo_dedicacion(self, data, **kwargs):
        return TipoDedicacion(**data)