from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile


def create_pdf(notes):

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")

    c = canvas.Canvas(temp_file.name, pagesize=letter)

    text_object = c.beginText(40, 750)

    for line in notes.split("\n"):
        text_object.textLine(line)

    c.drawText(text_object)
    c.save()

    return temp_file.name