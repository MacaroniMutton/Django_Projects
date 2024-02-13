from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=200)
    carbs = models.FloatField()
    proteins = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()

    def __str__(self):
        return self.name
    
class Consume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} consumes {self.food_consumed}"
    
class Goal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    goal = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user}'s Goal: {self.goal}"