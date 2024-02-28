from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from .utils import generate_certificate
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import Student

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('registration_success')
    else:
        form = StudentForm()
    return render(request, 'workshop_app/register_student.html', {'form': form})

def registration_success(request):
    return render(request, 'workshop_app/registration_success.html')

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

from .models import Student

def generate_certificate(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'workshop_app/generate_certificate.html', {'student': student})




def download_certificate(request, student_id):
    # Assuming Student model has 'name' attribute
    student = get_object_or_404(Student, id=student_id)

    # Create a response object with PDF MIME type
    response = HttpResponse(content_type='application/pdf')

    # Set the file name for the PDF download
    response['Content-Disposition'] = f'attachment; filename="{student.name}_certificate.pdf"'

    # Create a canvas with landscape page size
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # Add a border to the certificate
    border_padding = 20
    p.setStrokeColor(colors.black)
    p.setLineWidth(2)
    p.rect(border_padding, border_padding, width - 2 * border_padding, height - 2 * border_padding)

    # Add certificate title
    p.setFont("Helvetica-Bold", 24)
    title_text = "Certificate of Participation"
    title_width = p.stringWidth(title_text, "Helvetica-Bold", 24)
    p.drawCentredString(width / 2, height - 2 * border_padding, title_text)

    # Add student's name
    p.setFont("Helvetica-Bold", 16)
    p.drawString(border_padding + 30, height - 120, f"This is to certify that {student.name}")

    # Add participation message
    p.setFont("Helvetica", 14)
    p.drawString(border_padding + 30, height - 150, "has successfully participated in the workshop.")

    # Add signature lines
    signature_line_y = 100
    p.line(border_padding + 30, signature_line_y, width - border_padding - 30, signature_line_y)
    p.drawString(border_padding + 30, signature_line_y - 20, "Signature of HOD")
    p.drawString(width - border_padding - 150, signature_line_y - 20, "Signature of Speaker")

    # Save the PDF
    p.save()

    return response

