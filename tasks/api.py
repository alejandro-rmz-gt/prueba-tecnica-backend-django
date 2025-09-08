from rest_framework import viewsets, permissions
from .models import TasksModel
from .serializers import TasksSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = TasksModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TasksSerializer
