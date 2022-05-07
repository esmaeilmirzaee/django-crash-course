from django.urls import path
from .views import todo_home_view

urlpatterns = [
    path('', todo_home_view)
]
