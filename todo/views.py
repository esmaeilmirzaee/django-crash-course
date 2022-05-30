from django.shortcuts import render, redirect

from todo.forms import TodoForm
from .models import Todo


# Retrieve list of todos
def todo_home_view(request):
    tasks = Todo.objects.all()
    context = {
        'tasks': None,
    }
    if tasks:
        context['tasks'] = tasks
    return render(request, "todo/home.html", context=context)


# Retrieve a todo
def todo_detail_view(request, id: int):
    context = {
        'task': None
    }
    task = Todo.objects.get(id=id)
    context['task'] = task
    return render(request, 'todo/detail.html', context=context)


# Create
def todo_create_view(request):
    context = {'form': None}
    form = TodoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')

    context['form'] = form
    return render(request, 'todo/create.html', context=context)


def todo_update_view(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/', id)

    context = {'form': form}
    return render(request, 'todo/update.html', context)


def todo_delete_view(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
