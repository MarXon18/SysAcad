from marshmallow import Schema, fields, post_load, validate
from app.models import TipoEspecialidad

class TipoEspecialidadMapping(Schema):
    hashid = fields.String(dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))

    @post_load
    def nuevo_plan(self, data, **kwargs):
        return TipoEspecialidad(**data)