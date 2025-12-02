from marshmallow import Schema, fields, post_load, validate
from app.models import Grado
from markupsafe import escape

class GradoMapping(Schema):
    hashids = fields.String(dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))

    @post_load
    def nuevo_grado(self, data, **kwargs):
        for key in ['nombre']:
            if key in ['nombre']:
                data[key]= escape(data[key])
        return Grado(**data)