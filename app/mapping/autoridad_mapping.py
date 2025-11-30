from marshmallow import Schema, fields, post_load, validate
from app.models.autoridad import Autoridad

class AutoridadMapping(Schema):
    hashid = fields.String(attribute="hashid", dump_only=True)
    nombre= fields.String(required=True, validate=validate.Length(min=1,max=50))
    telefono= fields.String(required=True, validate=validate.Length(min=1,max=20))
    email= fields.String(required=True, validate=validate.Length(min=1,max=100))
    cargo_id= fields.Integer(required=True)
    cargo = fields.Nested('CargoMapping', only=('hashids', 'nombre'), dump_only=True)   

    @post_load
    def nueva_autoridad(self, data, **kwargs):
        return Autoridad(**data)
    
