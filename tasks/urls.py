from django.urls import path
from .views import TasksListAPI

urlpatterns = [
    path('api/v1/tasks', TasksListAPI.as_view())
]
