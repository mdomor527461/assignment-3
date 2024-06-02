from django.db import models
# from task import models
# Create your models here.
class CategoryModel(models.Model):
    categoryName = models.CharField(max_length=255)
    
    # task = models.ManyToManyField(models.TaskModel)
    
    def __str__(self):
        return self.categoryName
