from django.urls import path
from . import views

urlpatterns = [
    path('examcontroller1/', views.examcontroller1, name='examcontroller1'),
    path('examcontroller_get_info/', views.examcontroller_get_info, name='examcontroller_get_info'),
    path('examcontroller_login/', views.examcontroller_login, name='examcontroller_login'),
    path('examcontroller_emnei/', views.examcontroller_emnei, name='examcontroller_emnei')
]