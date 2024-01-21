from django.shortcuts import render, redirect
from .models import Employee, Department, EmployeeSalary
from django.contrib import messages
from django.db.models import Sum

# Create your views here.

def home(request):
    return render(request, "base.html")

# Employee Module

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

def edit_employee(request, emp_id):
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        designation = request.POST['designation']
        report_to = request.POST['reportto']
        department_id = request.POST['department']
        report_manager = Employee.objects.get(id = report_to)
        department = Department.objects.get(id = department_id)

        employee = Employee.objects.get(id = emp_id)
        employee.name = name
        employee.email = email
        employee.address = address
        employee.designation = designation
        employee.reporting_manager = report_manager
        employee.department = department
        employee.save()

        messages.success(request,"Employee updated successfully !")

        return redirect('/')
    else:
        employee = Employee.objects.get(id = emp_id)
        all_employees = Employee.objects.all()
        designation_choices = Employee.DESIGNATION_CHOICES
        departments = Department.objects.all()
        context = {
            'employee': employee,
            'all_employees' : all_employees,
            'designation_choices': designation_choices,
            'departments': departments,
        }
    return render(request,"edit_employee.html", context)

def del_employee(request, emp_id):
    employee = Employee.objects.get(id = emp_id)
    employee.delete()
    messages.success(request,"Employee deleted successfully !")
    return redirect('/employees/')



def employees(request):
    employees = Employee.objects.all()
    context = {'employees' : employees}
    return render(request,"employees.html", context)


# Department Module

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

def edit_department(request, dep_id):
    
    if request.method == 'POST':
        name = request.POST['name']
        floor = request.POST['floor']

        set_dep = Department.objects.get(id = dep_id)
        set_dep.name = name
        set_dep.floor = floor
        set_dep.save()

        messages.success(request,"Department updated successfully !")
        return redirect('/departments')
    else:
        department = Department.objects.get(id = dep_id)
        context = {'department' : department}
        return render(request,"edit_department.html", context)

def del_department(request, dep_id):
    department = Department.objects.get(id = dep_id)
    department.delete()
    messages.success(request,"Department deleted successfully !")
    return redirect('/departments/')

def departments(request):
    departments = Department.objects.all()
    context = {'departments' : departments}
    return render(request,"departments.html", context)


def check_hierarchy(request, dep_id):
    if request.method == 'POST':
        try:
            team_lead_id = request.POST['team_lead_id']
            lead = Employee.objects.get(id = team_lead_id)

            department  = Department.objects.get(id = dep_id)
            manager = Employee.objects.get(department = department, designation='Manager')
            team_leads = Employee.objects.filter(department = department, designation='TL')
            associates = Employee.objects.filter(department = department, designation='Associate', reporting_manager = lead)
            context = {
                'manager' : manager,
                'team_leads' : team_leads,
                'associates' : associates,
                'department': department
            }
        except Employee.DoesNotExist:
            messages.error(request,"Manager not found for this department !")
            return render(request, "hierarchy.html", {'error_message': 'Department not found'})

        return render(request,"hierarchy.html", context)

    else:
        try:
            department  = Department.objects.get(id = dep_id)
            manager = Employee.objects.get(department = department, designation='Manager')
            team_leads = Employee.objects.filter(department = department, designation='TL')
            context = {
                'manager' : manager,
                'team_leads' : team_leads,
                'department': department
            }
        except Employee.DoesNotExist:
            messages.error(request,"Manager not found for this department !")
            return render(request, "hierarchy.html", {'error_message': 'Department not found'})

        return render(request,"hierarchy.html", context)


# Salary Module

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


def edit_salary(request, sal_id):
    employee = EmployeeSalary.objects.get(id = sal_id)
    context = {'employee' : employee}
    if request.method == "POST":
        employee_id = request.POST['employee_id']
        salary = request.POST['salary']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        employee = Employee.objects.get(id = employee_id)

        set_salary = EmployeeSalary.objects.get(id = sal_id)
        set_salary.employee = employee
        set_salary.salary = salary
        set_salary.start_date = start_date
        set_salary.end_date = end_date
        set_salary.save()
        messages.success(request,"Salary updated successfully !")
        return redirect('/salary')


    return render(request,"edit_salary.html", context)

def del_salary(request, sal_id):
    salary = EmployeeSalary.objects.get(id = sal_id)
    salary.delete()
    messages.success(request,"Salary record deleted successfully !")
    return redirect('/salary/')

def dep_salary(request):

    if request.method == 'POST':
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']

        # Get all departments
        all_departments = Department.objects.all()

        # Use aggregation to calculate the total salary for each department within the specified date range
        department_totals = EmployeeSalary.objects.filter(
            start_date__gte=start_date,
            end_date__lte=end_date
        ).values('employee__department__name').annotate(total_salary=Sum('salary'))

        # Create a dictionary to store total salary for each department
        department_totals_dict = {entry['employee__department__name']: entry['total_salary'] for entry in department_totals}

        # Add departments with zero total salary
        for department in all_departments:
            department_name = department.name
            if department_name not in department_totals_dict:
                department_totals_dict[department_name] = 0

        # Create a list of dictionaries to pass to the template
        department_totals_list = [{'department_name': department_name, 'total_salary': total_salary} for department_name, total_salary in department_totals_dict.items()]

        # Assuming you want to display the results in a template
        return render(request, "dep_salary.html", {'departments': department_totals_list})

    else:
        
        # Get all departments
        all_departments = Department.objects.all()

        # Use aggregation to calculate the total salary for each department
        department_totals = EmployeeSalary.objects.values('employee__department__name').annotate(total_salary=Sum('salary'))

        # Create a dictionary to store total salary for each department
        department_totals_dict = {entry['employee__department__name']: entry['total_salary'] for entry in department_totals}

        # Add departments with zero total salary
        for department in all_departments:
            department_name = department.name
            if department_name not in department_totals_dict:
                department_totals_dict[department_name] = 0

        # Create a list of dictionaries to pass to the template
        department_totals_list = [{'department_name': department_name, 'total_salary': total_salary} for department_name, total_salary in department_totals_dict.items()]

        # Assuming you want to display the results in a template
        return render(request, "dep_salary.html", {'departments': department_totals_list})
    
def salary(request):
    emp_salary = EmployeeSalary.objects.all()
    context = {'salary' : emp_salary}
    return render(request,"salary.html", context)