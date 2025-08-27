
from flask import Blueprint, request, jsonify, send_file
from app.models.alumno import Alumno
from app import db
from app.formatters.json_formatter import AlumnoJSONFormatter
from app.formatters.pdf_formatter import AlumnoPDFFormatter

alumno_bp = Blueprint('alumno', __name__)

@alumno_bp.route('/alumnos/<int:alumno_id>/ficha', methods=['GET'])
def get_ficha(alumno_id):
    alumno = db.session.get(Alumno, alumno_id)
    if not alumno:
        return jsonify({"error": "Alumno no encontrado"}), 404

    formato = request.args.get("formato", "json")

    if formato == "pdf":
        formatter = AlumnoPDFFormatter()
        pdf_buffer = formatter.format(alumno)
        return send_file(pdf_buffer, mimetype="application/pdf", as_attachment=True, download_name="ficha_alumno.pdf")

    # default JSON
    formatter = AlumnoJSONFormatter()
    return jsonify(formatter.format(alumno))
