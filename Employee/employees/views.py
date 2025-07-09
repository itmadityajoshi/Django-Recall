from django.shortcuts import render, HttpResponse
from django.http import Http404
from .models import Employee

# Create your views here.


def employee_detail(req, pk):
    try:
        employee = Employee.objects.get(pk=pk)
        context = {
            'employee' : employee
        }
        return render(req, 'employee_detail.html', context)
    except:
        raise Http404

