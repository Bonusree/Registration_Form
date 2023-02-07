from django.urls import path
from . import views

urlpatterns = [
    path('chairman/', views.chairman, name='chairman'),
   
]