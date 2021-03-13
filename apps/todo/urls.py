from django.urls import path

from apps.todo.views import ListTaskCategory, DueLatestTask, AddTask, AddCategory, DetailTask, ListTask, \
    TaskUpdate, TaskListEdit, list_category

# ListCategory
urlpatterns = [
    # path('category_list/', ListCategory.as_view(), name='categorylist'),
    path('category_list/', list_category, name='categorylist'),

    path('due_task_list/', DueLatestTask.as_view(), name='tasklist'),
    path('<int:pk>/', ListTaskCategory.as_view(), name='list_task_category'),
    path('add_task/', AddTask.as_view(), name='addtask'),
    path('add_category/', AddCategory.as_view(), name='addcategory'),
    path('task_list/<int:pk>/', DetailTask.as_view(), name='taskdetail'),
    path('task_list/', ListTask.as_view(), name='fultasklist'),
    path('task_list_edit/', TaskListEdit.as_view(), name='tasklistedit'),
    path('<pk>/update_task/', TaskUpdate.as_view(), name='taskupdate'),


]
