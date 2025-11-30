from marshmallow import Schema, fields, post_load, validate
from app.models.nota import Nota

class NotaMapping(Schema):
    hashid= fields.String(dump_only=True)
    calificacion = fields.String(required=True, validate=validate.Length(min=1, max=10))

    @post_load
    def nueva_nota(self,data, **kwargs):
        return Nota(**data)
