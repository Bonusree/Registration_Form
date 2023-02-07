from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student, name='student'),
    path('registration/', views.registration1, name='student_registration1'),
    path('image/', views.image, name='image'),
    path('pdfoo/', views.generate_pdf)
]