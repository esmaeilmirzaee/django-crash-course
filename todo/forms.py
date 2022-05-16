from distutils.command.clean import clean
from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['due_date', 'task_name']

    def clean(self):
        cleaned_data = self.cleaned_data

        if cleaned_data.get('task_name').lower().strip() == 'xxxx':
            print('task name', cleaned_data.get('task_name'))
            self.add_error('task_name', 'Unacceptable keywords')

        return cleaned_data
