from django.contrib import admin

from apps.todo.models.task import Task, Category


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'description', 'priority', 'due_date', 'category', 'done']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    prepopulated_fields = {'slug': ('name',)}
