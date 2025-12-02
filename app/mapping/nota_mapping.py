from marshmallow import Schema, fields, post_load, validate
from app.models.nota import Nota
from markupsafe import escape #importar para sanitizacion

class NotaMapping(Schema):
    hashids= fields.String(attribute="hashid", dump_only=True)
    calificacion = fields.String(required=True, validate=validate.Length(min=1, max=10))

    @post_load
    def nueva_nota(self,data, **kwargs):
        #sanitizacion del campo de texto antes de crear la instancia
        for key in ['calificacion']:
            if key in data:
                data[key] = escape(data[key])
        return Nota(**data)
        
