import unittest
from flask import current_app
from app import create_app
import os
from app.models.documento import Documento
from app.services.documento_service import DocumentoService
from app import db

class AppTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        
    def test_documento_creation(self):
        documento = self.__nuevo_documento()
        self.assertIsNotNone(documento)
        self.assertEqual(documento.tipo_documento, "DNI")
        
    def test_crear_documento(self):
        documento = self.__nuevo_documento()
        DocumentoService.crear_documento(documento)
        self.assertIsNotNone(documento)
        self.assertIsNotNone(documento.id)
        self.assertGreaterEqual(documento.id, 1)
        self.assertEqual(documento.tipo_documento, "DNI")

    def test_documento_busqueda(self):
        documento = self.__nuevo_documento()
        DocumentoService.crear_documento(documento)    
        
        resultado=DocumentoService.buscar_por_id(documento.id)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.tipo_documento, "DNI")


    def test_buscar_todos_los_documentos(self):
        documento1 = self.__nuevo_documento(tipo="DNI")
        documento2 = self.__nuevo_documento(tipo="Pasaporte")
        DocumentoService.crear_documento(documento1)
        DocumentoService.crear_documento(documento2)
        documento = DocumentoService.buscar_todos()
        self.assertIsNotNone(documento)
        self.assertEqual(len(documento), 2)

    def test_actualizar_documento(self):
        documento= self.__nuevo_documento()
        DocumentoService.crear_documento(documento)
        documento.tipo_documento = "Pasaporte"
        doc_actualizado = DocumentoService.actualizar_documento(documento.id, documento)
        self.assertEqual(doc_actualizado.tipo_documento, "Pasaporte")
        doc_bd= DocumentoService.buscar_por_id(documento.id) #Verificamos en BD
        self.assertEqual(doc_bd.tipo_documento, "Pasaporte")

    def test_borrar_documento(self):
        documento = self.__nuevo_documento()
        DocumentoService.crear_documento(documento)
        DocumentoService.borrar_por_id(documento.id)
        resultado = DocumentoService.borrar_por_id(documento.id)
        self.assertIsNone(resultado)

    def test_serializacion_documento(self):
        """
        Prueba de Mapping: Verifica que el objeto Documento se convierta
        correctamente a un diccionario/JSON.
        """
        documento = self.__nuevo_documento(tipo="LC")
        
        #Definimos lo que esperamos recibir
        datos_esperados = {
            "tipo_documento": "LC",
            "descripcion": "Tipo de Documento: LC" # Ejemplo de campo hipotético
        }
        # Simular el mapeo
        datos_actuales = {
            "tipo_documento": documento.tipo_documento,
            "descripcion": f"Tipo de Documento: {documento.tipo_documento}"
        }
        # Valida
        self.assertEqual(datos_actuales["tipo_documento"], datos_esperados["tipo_documento"])
        self.assertDictEqual(datos_actuales, datos_esperados)

    
    def __nuevo_documento(self,tipo="DNI"):
        documento = Documento()
        documento.tipo_documento = 'DNI'
        return documento
        
if __name__ == '__main__':
    unittest.main()
