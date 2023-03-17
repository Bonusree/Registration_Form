from django.urls import path
from . import views

urlpatterns = [
    path('hallprovost1/', views.hallprovost1, name='hallprovost1'),
    path('hallprovost_get_info/', views.hallprovost_get_info, name='hallprovost_get_info'),
    path('hallprovost_login/', views.hallprovost_login, name='hallprovost_login'),
    path('hallprovost_ac/', views.hallprovost_ac, name='hallprovost_ac')
]