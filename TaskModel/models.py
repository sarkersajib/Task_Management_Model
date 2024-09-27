from django.db import models
from TaskCategory.models import TaskCategory

# Create your models here.
class TaskModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    AssignDate = models.DateField()
    category = models.ManyToManyField(TaskCategory)

    def __str__(self):
        return self.title
    