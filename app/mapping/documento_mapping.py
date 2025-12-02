from marshmallow import Schema, fields, post_load, validate
from app.models.documento import Documento

class DocumentoMapping(Schema):
    id= fields.Integer(dump_only=True)
    tipo_documento = fields.String(required=True, validate=validate.Length(min=1, max=50))

    @post_load
    def nuevo_documento(self, data, **kwargs):
        return Documento(**data)
    