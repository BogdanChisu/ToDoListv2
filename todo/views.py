from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task

# Create your views here.


def addTask(request):
    name_task = request.POST['task']
    # new_task = Task(task=name_task)
    # new_task.save()
    new_task = Task.objects.create(task=name_task)
    return redirect('home')

def mark_as_done(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request, pk):
    get_task = Task.objects.get(pk=pk)
    if request.method == "POST":
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        print(new_task)
        return redirect('home')
    else:
        context = {
            'get_task': get_task,
        }
        return render(request, 'edit_task.html', context)

def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('home')
