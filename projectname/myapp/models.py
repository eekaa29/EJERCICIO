from django.db import models

# Create your models here.
from django.db import models
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class User(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.IntegerField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name
    


    
