# from django.http import HttpResponse
from django.shortcuts import render

from todo.models import Task


def home(request):
    # return HttpResponse('<h1>Homepage</h1>')

    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    # -updated_at - to see the tasks in descending order of update from the most
    # recent to the first one
    # for task in tasks:
    #     print(task.task)

    completed_tasks = Task.objects.filter(is_completed=True)
    # print(completed_tasks)

    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
    }
    return render(request, 'home.html', context)