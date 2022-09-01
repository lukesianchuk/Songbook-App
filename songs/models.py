from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.TextField()
    instrument = models.CharField(max_length=20)
    #image = models.FilePathField(path="songs/static/img")
    chordlink = models.URLField(default="https://www.ultimate-guitar.com/")
    media = models.ImageField(blank=True)