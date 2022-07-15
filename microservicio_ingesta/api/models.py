from django.db import models

# Create your models here.

class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    age = models.IntegerField()
    password = models.CharField(max_length=100)
    
class Comics(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    image = models.URLField()
    onsaleDate = models.DateTimeField()
    user_id = models.IntegerField()
