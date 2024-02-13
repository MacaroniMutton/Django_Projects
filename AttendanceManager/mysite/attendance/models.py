from django.db import models
from datetime import datetime
from django.conf import settings

# Create your models here.

class Subject(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=200)
    classes_attended = models.IntegerField(default=0)
    total_classes = models.IntegerField(default=0)
    percentage = models.FloatField(default=100)
    curr_status = models.CharField(max_length=200, default="No ongoing classes")

    class Meta:
        unique_together = ('user', 'name')

    def __str__(self):
        return self.name
    
class SubjectReport(models.Model):
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=datetime.now, blank=True)
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.subject.name
    
    def subject_curr_status(self):
        return self.subject.curr_status