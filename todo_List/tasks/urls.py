from django.urls import path
from . import views

urlpatterns = [
    path('tasks_list/', views.tasks_list, name='tasks_list'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/<int:pk>/update/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
]
