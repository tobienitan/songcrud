
from django.db import models
from datetime import datetime

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()
    

class song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    date_released = models.DateField(default=datetime.today)
    likes = models.IntegerField()
    artisteId = models.IntegerField()
    

class lyric(models.Model):
    song = models.ForeignKey(song, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    songId = models.IntegerField()
   
    



