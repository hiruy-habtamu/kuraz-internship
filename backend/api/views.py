from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Task
from .serializers import TaskSerializer, TaskListSerializer

class TaskCreateListAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer

class TaskRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer