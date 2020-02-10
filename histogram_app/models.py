from django.db import models

# Create your models here.

''' Pass data to the database. '''
class Data(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.IntegerField()
