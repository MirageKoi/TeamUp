from django.shortcuts import render
from .serializers import TasksSerializer
from .models import TasksModel
from rest_framework.generics import ListCreateAPIView


class TasksListAPI(ListCreateAPIView):
    queryset = TasksModel.objects.all()
    serializer_class = TasksSerializer



