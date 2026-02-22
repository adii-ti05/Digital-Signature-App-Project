from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
import io

def add_signature_to_pdf(input_path, output_path, signature_text, x, y):
    packet = io.BytesIO()
    can = canvas.Canvas(packet)
    can.drawString(x, y, signature_text)
    can.save()

    packet.seek(0)
    new_pdf = PdfReader(packet)
    existing_pdf = PdfReader(open(input_path, "rb"))
    output = PdfWriter()

    page = existing_pdf.pages[0]
    page.merge_page(new_pdf.pages[0])
    output.add_page(page)

    with open(output_path, "wb") as outputStream:
        output.write(outputStream)