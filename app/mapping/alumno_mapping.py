from marshmallow import Schema, fields, validate, post_load
from app.models import Alumno

class AlumnoMapping(Schema):
    hashid = fields.String(dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=50))
    apellido = fields.String(required=True, validate=validate.Length(min=1, max=50))
    fecha_nacimiento = fields.Date(required=True)
    nro_documento = fields.String(required=True, validate=validate.Length(min=1, max=50))
    sexo = fields.String(required=True, validate=validate.Length(equal=1))
    nro_legajo = fields.Integer(required=True)
    fecha_ingreso = fields.Date(required=True)
    tipo_documento_id = fields.Integer(required=True)

    @post_load
    def nuevo_alumno(self, data, **kwargs):
        return Alumno(**data)