from django.db import models
import uuid

class Data(models.Model):
    mes=models.JSONField()
class Event(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    Venue = models.CharField(max_length=50)
    date_time = models.DateTimeField()
    date_time1 = models.DateTimeField(null=True)
    department = models.CharField(max_length=100,null=True, blank=True)
    coordinator_name = models.CharField(max_length=50,null=True, blank=True)
    person = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.title} on {self.date_time}"

