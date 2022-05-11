from django.db import models


class Todo(models.Model):
    task_name = models.CharField(max_length=100)
    due_date = models.DateField()
    created_at = models.DateField(
        auto_now_add=True, auto_created=True)

    def __str__(self):
        return self.task_name
