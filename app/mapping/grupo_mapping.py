from marshmallow import Schema, fields, validate, post_load
from app.models import Grupo
from markupsafe import escape

class GrupoMapping(Schema):
    id= fields.Integer(dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    grado_id = fields.Int(allow_none=True)

    @post_load
    def nuevo_grupo(self, data, **kwargs) :
        for campo in ['nombre']:
            if isinstance(data.get(campo), str):
                data[campo] = escape(data[campo])
        return Grupo(**data)