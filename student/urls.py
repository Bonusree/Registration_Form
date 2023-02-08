from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student, name='student'),
    path('regi_show/', views.regi_show, name='regi_show'),
    path('regicomplete/', views.regi_complete, name='regicomplete'),
]