from django.urls import path
from . import views

urlpatterns = [
    path('chairman1/', views.chairman1, name='chairman1'),
    path('chairman_get_info/', views.chairman_get_info, name='chairman_get_info'),
    path('chairman_login/', views.chairman_login, name='chairman_login'),
    path('chairman_ac/', views.chairman_ac, name='chairman_ac')
]