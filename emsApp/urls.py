from django.urls import path
from emsApp import views


urlpatterns = [
    path('', views.home),
    path('add/employee/', views.add_emp),
    path('edit/employee/<int:emp_id>', views.edit_employee),
    path('delete/employee/<int:emp_id>', views.del_employee),
    path('employees/', views.employees),
    path('add/department/', views.add_department),
    path('edit/department/<int:dep_id>', views.edit_department),
    path('delete/department/<int:dep_id>', views.del_department),
    path('hierarchy/<int:dep_id>', views.check_hierarchy),
    path('departments/', views.departments),
    path('add/salary/', views.add_salary),
    path('edit/salary/<int:sal_id>', views.edit_salary),
    path('delete/salary/<int:sal_id>', views.del_salary),
    path('salary/', views.salary),
    path('department/salary/', views.dep_salary),
]