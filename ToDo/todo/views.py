from django.shortcuts import render
from addTask.models import *
def home(req):
    tasks = AddTask.objects.filter(is_completed= False)
    # print(task)



    #to show completed task
    completed = AddTask.objects.filter(is_completed=True)
    context = {
        'tasks': tasks,
        'complete': completed
    }
    return render(req, 'home.html', context)