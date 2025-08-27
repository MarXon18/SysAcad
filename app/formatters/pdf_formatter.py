
from app.formatters.base_formatter import IAlumnoFormatter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

class AlumnoPDFFormatter(IAlumnoFormatter):
    def format(self, alumno):
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer)
        styles = getSampleStyleSheet()
        story = []

        story.append(Paragraph(f"Ficha del Alumno", styles['Title']))
        story.append(Spacer(1, 12))
        story.append(Paragraph(f"Nro Legajo: {alumno.nro_legajo}", styles['Normal']))
        story.append(Paragraph(f"Apellido: {alumno.apellido}", styles['Normal']))
        story.append(Paragraph(f"Nombre: {alumno.nombre}", styles['Normal']))
        story.append(Paragraph(f"Facultad: {alumno.facultad.nombre}", styles['Normal']))

        doc.build(story)
        buffer.seek(0)
        return buffer
