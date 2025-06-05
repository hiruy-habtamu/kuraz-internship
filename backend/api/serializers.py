from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'status']
    def validate_title(self, value):
        if not value or value.strip() == "":
            raise serializers.ValidationError("Title must not be empty.")
        return value