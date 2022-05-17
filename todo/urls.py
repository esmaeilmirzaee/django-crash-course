from django.urls import path
from .views import (
    todo_create_view,
    todo_home_view,
    todo_detail_view,
    todo_update_view
)

urlpatterns = [
    path('', todo_home_view),
    path('<int:id>/', todo_detail_view),
    path('create/', todo_create_view),
    path('<int:id>/update', todo_update_view)
]
