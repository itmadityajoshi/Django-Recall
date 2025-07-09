from django.shortcuts import render

from employees.models import Employee


def home(req):
    employees = Employee.objects.all()
    # print(employees)
    context = {
        'employees' : employees,
    }
    return render(req, 'home.html', context)