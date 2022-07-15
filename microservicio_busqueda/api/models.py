from django.db import models

# Create your models here.

# class Personajes(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     name = models.CharField(max_length=255)
#     image = models.URLField()
#     appearances = models.IntegerField()
    
class Personajes:
  def __init__(self, id, name, image, appearances):
    self.id = id
    self.name = name
    self.image = image
    self.appearances = appearances
    
class Comics:
  def __init__(self, id, title, image, onsaleDate):
    self.id = id
    self.title = title
    self.image = image
    self.onsaleDate = onsaleDate
