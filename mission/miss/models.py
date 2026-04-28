from django.db import models

# Create your models here.
class Habit(models.Model):
    name = models.CharField(max_length=200)
    task_date = models.DateField()
    completed = models.BooleanField(default=False)