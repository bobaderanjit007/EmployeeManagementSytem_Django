from django.urls import path
from emsApp import views


urlpatterns = [
    path('', views.home),

    # Employee View
    path('add/employee/', views.add_emp, name="add_emp"),
    path('edit/employee/<int:emp_id>', views.edit_employee, name="edit_employee"),
    path('delete/employee/<int:emp_id>', views.del_employee, name="del_employee"),
    path('employees/', views.employees, name="employee"),

    # Department View
    path('add/department/', views.add_department, name="add_department"),
    path('edit/department/<int:dep_id>', views.edit_department, name="edit_department"),
    path('delete/department/<int:dep_id>', views.del_department, name="del_department"),
    path('hierarchy/<int:dep_id>', views.check_hierarchy, name="check_hierarchy"),
    path('departments/', views.departments, name="departments"),

    # Salary View
    path('add/salary/', views.add_salary, name="add_salary"),
    path('edit/salary/<int:sal_id>', views.edit_salary, name="edit_salary"),
    path('delete/salary/<int:sal_id>', views.del_salary, name="del_salary"),
    path('salary/', views.salary, name="salary"),
    path('department/salary/', views.dep_salary, name="dep_salary"),
]