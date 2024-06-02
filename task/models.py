from django.db import models
from category.models import CategoryModel
# Create your models here.
class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=255)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    taskAssignDate = models.DateField()
    
    category = models.ManyToManyField(CategoryModel)
    def __str__(self):
        return self.taskTitle