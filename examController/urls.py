from django.urls import path
from . import views

urlpatterns = [
    path('examcontroller/', views.examcontroller, name='examcontroller'),
   
]