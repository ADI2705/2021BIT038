from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_student, name='register_student'),
    path('registration-success/', views.registration_success, name='registration_success'),
    path('generate-certificate/<int:student_id>/', views.generate_certificate, name='generate_certificate'),
    path('download-certificate/<int:student_id>/', views.download_certificate, name='download_certificate'),
    # Add other URLs as needed
]
