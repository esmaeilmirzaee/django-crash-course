from django.urls import path
from .views import todo_home_view, todo_detail_view

urlpatterns = [
    path('', todo_home_view),
    path('<int:id>/', todo_detail_view),
]
