from reportlab.pdfgen import canvas
from django.http import HttpResponse

def generate_certificate(student):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="certificate.pdf"'

    p = canvas.Canvas(response)
    p.drawString(100, 100, f"Certificate of Participation\n\nThis is to certify that {student.name} attended the workshop.")
    p.showPage()
    p.save()

    return response
