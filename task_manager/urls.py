from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'task_manager'

urlpatterns = [
    path('task', views.task, name='task'),
]