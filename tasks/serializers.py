from rest_framework import serializers
from .models import TasksModel

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasksModel
        fields = ("title", "description", "is_completed", "created_at")
        read_only_fields = ("created_at",)
