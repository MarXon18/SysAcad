from flask import Blueprint, jsonify, request
from app.mapping.alumno_mapping import AlumnoMapping
from app.services.alumno_service import AlumnoService
from app.validators import validate_with
import logging

logging.basicConfig(level=logging.DEBUG)

alumno_bp = Blueprint('alumno', __name__)
alumno_mapping = AlumnoMapping()

#GET/alumno/ <id>
@alumno_bp.route('/alumno/<int:id>', methods=['GET'])
def buscar_por_id(id):
    alumno= AlumnoService.buscar_por_id(id)
    if alumno is None:
        return jsonify({"error": "Alumno no encontrado"}), 404
    return alumno_mapping.dump(alumno),200

#GET /alumno
@alumno_bp.route('/alumno', methods=['GET'])
def listar_alumnos():
    alumnos = AlumnoService.buscar_todos()
    return alumno_mapping.dump(alumnos, many=True),200

#POST /alumno
@alumno_bp.route('/alumno', methods=['POST'])
@validate_with(AlumnoMapping)
def crear(data):
    alumno = alumno_mapping.load(data)
    AlumnoService.crear_alumno(alumno)
    return jsonify({"mensaje": "Alumno creado correctamente"}),201

#PUT /alumno/ <id>
@alumno_bp.route('/alumno/<int:id>', methods=['PUT'])
@validate_with(AlumnoMapping)
def actualizar(data,id):
    alumno = alumno_mapping.load(data)
    actualizado = AlumnoService.actualizar_alumno(id,alumno)
    
    if actualizado is None:
        return jsonify({"error": "Alumno no encontrado"}), 404
    return jsonify({"mensaje": "Alumno actualizado correctamente"}), 200

# DELETE /alumno/<id>
@alumno_bp.route('/alumno/<int:id>', methods= ['DELETE'])
def borrar(id):
    eliminado = AlumnoService.borrar_por_id(id)
    if eliminado is None:
        return jsonify({"error": "Alumno no encontrado"}), 404
    return jsonify({"mensaje": "Alumno eliminado correctamente"}), 200
