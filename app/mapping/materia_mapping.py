from marshmallow import Schema, fields, post_load, validate
from app.models.materia import Materia
from app.mapping.nota_mapping import NotaMapping 

class MateriaMapping(Schema):
    hashid= fields.String(dump_only=True)
    nombre= fields.String(required=True, validate=validate.Length(min=1, max=100))
    codigo= fields.String(required=True, validate=validate.Length(min=1, max=100))
    observacion = fields.String(required=True, validate=validate.Length(min=1, max=100))

    nota_id = fields.Integer(allow_none=True)

    @post_load
    def nueva_materia(self,data, **kwargs):
        return Materia(**data)