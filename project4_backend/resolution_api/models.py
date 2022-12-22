from django.db import models

# Create your models here.
class Resolution(models.Model):
    title = models.CharField(max_length=40)
    image = models.CharField(max_length=500)
    description = models.CharField(max_length=999)
    category = models.CharField(max_length=100)
    accomplished = models.BooleanField()
