from django.db import models

# Create your models here.
class Playlist(models.Model):
  genre = models.CharField(max_length = 20)
  name = models.CharField(max_length = 30)
  pub_data = models.DateTimeField('data published')
  thumbnail = models.ImageField(upload_to = 'image')