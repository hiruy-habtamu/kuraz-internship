from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer, TaskListCreateSerializer

class TaskCreateListAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListCreateSerializer

class TaskRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        task.status = 'c'
        task.save()
        return Response({'detail': 'Task marked as completed.'}, status=status.HTTP_200_OK)