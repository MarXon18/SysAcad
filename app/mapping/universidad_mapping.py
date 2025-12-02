from marshmallow import Schema, fields, post_load, validate
from app.models import Universidad
from markupsafe import escape

class UniversidadMapping(Schema):
    hashids = fields.String(attribute="hashid",dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    sigla = fields.String(required=True, validate=validate.Length(min=1, max=5))
    facultad_id = fields.Int(allow_none=True)   

    @post_load
    def nueva_universidad(self, data, **kwargs): 
        for key in ['nombre', 'sigla']:
            if key in data:
                data[key] = escape(data[key])
        return Universidad(**data)