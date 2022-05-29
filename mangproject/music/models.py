from django.db import models

# Create your models here.
class Playlist(models.Model):
  genre = models.CharField(max_length = 20)
  name = models.CharField(max_length = 30)
  pub_date = models.DateTimeField('data published')
  thumbnail = models.ImageField(blank = True, upload_to = 'thumnail/%Y/%m/%d')