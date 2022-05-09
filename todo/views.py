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
