from django.shortcuts import render, redirect
from .models import AddTask
# Create your views here.

def addT(req):
    task = req.POST['task']
    AddTask.objects.create(task=task)
    return redirect('home')