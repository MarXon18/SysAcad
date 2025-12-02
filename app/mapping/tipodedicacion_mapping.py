from marshmallow import Schema, fields, post_load, validate
from app.models import TipoDedicacion
from markupsafe import escape

class TipoDedicacionMapping(Schema):
    id = fields.Integer()
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=50))
    observacion = fields.String(allow_none=True, validate=validate.Length(min=1, max=100))

    @post_load
    def nuevo_tipo_dedicacion(self, data, **kwargs):
        for key in ['nombre', 'observacion']:
            if key in data:
                data[key] = escape(data[key])
        return TipoDedicacion(**data)