from django.db import models

class Habit(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class HabitDay(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField()
    completed = models.BooleanField(default=False)