from django.db import models

class TasksModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_completed = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)