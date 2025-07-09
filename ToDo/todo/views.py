from django.shortcuts import render
from addTask.models import *
def home(req):
    tasks = AddTask.objects.filter(is_completed= False)
    # print(task)
    context ={
        'tasks': tasks
    }
    return render(req, 'home.html', context)