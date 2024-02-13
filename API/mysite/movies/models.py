from django.db import models

# Create your models here.

class MovieData(models.Model):
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    genre = models.CharField(max_length=200, default="action")
    image = models.ImageField(upload_to='Images/', default='noimg.png')

    def __str__(self):
        return self.name