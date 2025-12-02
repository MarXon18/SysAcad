from marshmallow import Schema, fields, post_load, validate
from app.models.materia import Materia
from markupsafe import escape

class MateriaMapping(Schema):
    id= fields.Integer(dump_only=True)
    nombre= fields.String(required=True, validate=validate.Length(min=1, max=100))
    codigo= fields.String(required=True, validate=validate.Length(min=1, max=100))
    observacion = fields.String(required=True, validate=validate.Length(min=1, max=100))

    nota_id = fields.Integer(allow_none=True)

    @post_load
    def nueva_materia(self,data, **kwargs):
        for key in ['nombre', 'codigo','observacion']:
            if key in data and isinstance(data[key],str):
                data[key]= escape(data[key])
        return Materia(**data)