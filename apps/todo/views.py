from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.views import View
from django.views.generic.edit import UpdateView

from apps.todo.forms import AddTaskModelForm, AddCategoryModelForm
from apps.todo.models import Category, Task


# this class view show all of task for edit
class TaskListEdit(ListView):
    model = Task
    template_name = 'todo/task_list_edit.html'


# this class update datails of task
class TaskUpdate(UpdateView):
    model = Task
    fields = ['title', 'description', 'priority', 'due_date', 'category', 'done', ]
    success_url = "/"


# this class show all of task
class ListTask(ListView):
    model = Task


# this task show detail of task
class DetailTask(DetailView):
    model = Task
    template_name = 'todo/task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# class ListCategory(TemplateView):  # list of category
#     template_name = 'todo/category_list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['full_category'] = Category.objects.get_full_category()
#         context['empty_category'] = Category.objects.get_empty_category()
#         return context
# this class show list of full and empty category
def list_category(request):
    context = {'full_category': Category.objects.get_full_category(),
               'empty_category': Category.objects.get_empty_category()}
    return render(request, 'todo/category_list.html', context)


# this class show list of tsk of category
class ListTaskCategory(DetailView):  # list task of category
    model = Category
    template_name = 'todo/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# this class show Due and latest task
class DueLatestTask(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_task'] = Task.objects.all()[:3]
        context['passed_task'] = Task.objects.get_passed_tasks()
        return context


# this class show a form for add task
class AddTask(View):  # a form for add task
    def get(self, request):
        form = AddTaskModelForm()
        return render(request, 'todo/add_task.html', {'form': form})

    def post(self, request):
        form = AddTaskModelForm(request.POST)
        if form.is_valid():
            validated_data = form.cleaned_data
            task_obj = Task(**validated_data)
            task_obj.save()
            return redirect('ok')
        return render(request, 'todo/add_category.html', {'form': form})


# this class show a form for add category
class AddCategory(View):  # a form for add category
    def get(self, request):
        form = AddCategoryModelForm()
        return render(request, 'todo/add_category.html', {'form': form})

    def post(self, request):
        form = AddCategoryModelForm(request.POST)
        if form.is_valid():
            validated_data = form.cleaned_data
            category_obj = Category(**validated_data)
            category_obj.save()
            return redirect('ok')
        return render(request, 'todo/add_task.html', {'form': form})


# this class is for download json file
class TaskListAPI(View):
    def get(self, request):
        serialized_person_list = serialize('json', Task.objects.all())
        return HttpResponse(serialized_person_list, content_type='application/json')
