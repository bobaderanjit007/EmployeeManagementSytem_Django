from django.shortcuts import render, redirect
from .models import Employee, Department, EmployeeSalary
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, "base.html")

def add_emp(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        designation = request.POST['designation']
        report_to = request.POST['reportto']
        department_id = request.POST['department']
        report_manager = Employee.objects.get(id = report_to)
        department = Department.objects.get(id = department_id)
        employee = Employee(name=name, email=email, address = address,
                            designation = designation, reporting_manager = report_manager,
                            department = department)
        employee.save()
        messages.success(request,"Employee added successfully !")

        return redirect('/')
    else:
        employees = Employee.objects.all()
        designation_choices = Employee.DESIGNATION_CHOICES
        departments = Department.objects.all()
        context = {
            'employees': employees,
            'designation_choices': designation_choices,
            'departments': departments,
        }
    return render(request,"add_emp.html", context)

def employees(request):
    employees = Employee.objects.all()
    context = {'employees' : employees}
    return render(request,"employees.html", context)



def add_department(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        floor = request.POST['floor']

        set_dep = Department(name = name, floor = floor)
        set_dep.save()

        messages.success(request,"Department added successfully !")
        return redirect('/departments')
    else:
        return render(request,"add_department.html")


def departments(request):
    departments = Department.objects.all()
    context = {'departments' : departments}
    return render(request,"departments.html", context)

def add_salary(request):
    employees = Employee.objects.all()
    context = {'employees' : employees}
    if request.method == "POST":
        employee_id = request.POST['employee']
        salary = request.POST['salary']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        employee = Employee.objects.get(id = employee_id)

        set_salary = EmployeeSalary(employee = employee, salary = salary,
        start_date = start_date, end_date = end_date)
        set_salary.save()
        messages.success(request,"Salary added successfully !")
        return redirect('/salary')


    return render(request,"add_salary.html", context)

def salary(request):
    emp_salary = EmployeeSalary.objects.all()

    context = {'salary' : emp_salary}

    return render(request,"salary.html", context)