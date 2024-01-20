from django.urls import path
from emsApp import views


urlpatterns = [
    path('', views.home),
    path('add/employee/', views.add_emp),
    path('employees/', views.employees),
    path('add/department/', views.add_department),
    path('departments/', views.departments),
    path('add/salary/', views.add_salary),
    path('salary/', views.salary),
]