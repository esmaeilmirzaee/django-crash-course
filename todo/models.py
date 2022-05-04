from django.db import models


class Todo(models.Model):
    task_name = models.CharField(max_length=100)
    due_date = models.DateField()

    def __str__(self):
        return self.task_name
