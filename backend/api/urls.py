from django.urls import path
from .views import TaskCreateListAPIView,TaskRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('tasks/', TaskCreateListAPIView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-retrieve-update-destroy'),
]