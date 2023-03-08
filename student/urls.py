from django.urls import path
from . import views

urlpatterns = [
    
    path('student1/', views.student1, name='student1'),
    path('student_login', views.student_login, name='student_login'),
    path('student_home/', views.student_home, name='student_home'),
    path('regicomplete/', views.regi_complete, name='regicomplete'),
    path('get_courses/', views.get_courses, name="get_courses"),
    path('get_admit_card/', views.get_admit_card, name="get_admit_card"),
    path('generate_pdf/', views.generate_pdf, name="generate_pdf")

 ]