from django import forms

from apps.todo.models import Task, Category


# this form is for task
class AddTaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'due_date', 'category', 'done']


# this form is for category
class AddCategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
