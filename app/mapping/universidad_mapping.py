from marshmallow import Schema, fields, post_load, validate
from app.models import Universidad

class UniversidadMapping(Schema):
    hashid = fields.String(dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    sigla = fields.String(required=True, validate=validate.Length(min=1, max=5))
    facultad_id = fields.Integer(allow_none=True)   

    @post_load
    def nueva_universidad(self, data, **kwargs): 
        return Universidad(**data)