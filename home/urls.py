from django.urls import path
from home import views 

urlpatterns = [
    path('', views.home),
    path('login/', views.doLogin, name='login'),
    path('add_student/',views.add_student,name="add_student"),
    path('add_student_save/', views.add_student_save,name="add_student_save"),
    path('add_chairman/',views.add_chairman,name="add_chairman"),
    path('add_chairman_save/', views.add_chairman_save,name="addchairman_save"),
    path('add_hallprovost/',views.add_hallprovost,name="add_hallprovost"),
    path('add_hallprovost_save/', views.add_hallprovost_save,name="add_hallprovost_save"),
    path('add_examcontroller/',views.add_examcontroller,name="add_examcontroller"),
    path('add_examcontroller_save/', views.add_examcontroller_save,name="add_examcontroller_save"),
    path('get_user_details', views.GetUserDetails),
]