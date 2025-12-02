from marshmallow import Schema, fields, post_load, validate
from app.models.facultad import Facultad
from markupsafe import escape

class FacultadMapping(Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    abreviatura = fields.String(required=True, validate=validate.Length(min=1, max=10))
    directorio= fields.String(required=True, validate=validate.Length(min=1, max=100))
    sigla = fields.String(required=True, validate=validate.Length(min=1, max=10))
    codigo_postal= fields.String(required=True, validate=validate.Length(min=1, max=10))
    ciudad = fields.String(required=True, validate=validate.Length(min=1, max=50))
    domicilio= fields.String(required=True, validate=validate.Length(min=1, max=100))
    telefono= fields.String(required=True, validate=validate.Length(min=1, max=20))
    contacto=fields.String(required=True, validate=validate.Length(min=1, max=100))
    email= fields.String(required=True, validate=validate.Length(min=1, max=100))

    @post_load
    def nueva_facultad(self, data, **kwargs):
        for key in ['nombre', 'abreviatura', 'directorio', 'sigla', 'codigo_postal', 'ciudad','domicilio','telefono','contacto', 'email']:
            if key in data:
                data[key] = escape(data[key])
        return Facultad(**data)