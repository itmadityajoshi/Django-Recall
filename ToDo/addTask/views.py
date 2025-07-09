from django.shortcuts import render, redirect, get_object_or_404
from .models import AddTask
# Create your views here.

def addT(req):

    #to add new task from client stide
    task = req.POST['task']
    AddTask.objects.create(task=task)
    return redirect('home')




def done(req,pk):
    task = get_object_or_404(AddTask, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def undo(req, pk):
    task = get_object_or_404(AddTask, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')


def edit(req, pk):
    get_tasks = get_object_or_404(AddTask, pk=pk)
    if req.method == "POST":
        new_task = req.POST['task']
        get_tasks.task = new_task
        get_tasks.save()
        return redirect('home')
    
    else:
        context ={
        'get_task': get_tasks
        }
        return render(req, 'edit.html', context)
    


def delete(req,pk):
    task = get_object_or_404(AddTask, pk=pk)
    task.delete()
    return redirect('home')