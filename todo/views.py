from django.shortcuts import render

from .models import Todo


def todo_home_view(request):
    tasks = Todo.objects.all()
    context = {
        'tasks': None,
    }
    if tasks:
        context['tasks'] = tasks
    return render(request, "todo/home.html", context=context)


def todo_detail_view(request, id: int):
    context = {
        'task': None
    }
    task = Todo.objects.get(id=id)
    context['task'] = task
    return render(request, 'todo/detail.html', context=context)
