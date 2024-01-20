from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=200)
    floor = models.IntegerField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.TextField()
    DESIGNATION_CHOICES = [
        ('Associate', 'Associate'),
        ('TL', 'Team Lead'),
        ('Manager', 'Manager'),
    ]
    designation = models.CharField(max_length=20, choices=DESIGNATION_CHOICES)
    reporting_manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class EmployeeSalary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.employee.name
