from django.shortcuts import render


def todo_home_view(request):

    return render(request, "todo/home.html")
