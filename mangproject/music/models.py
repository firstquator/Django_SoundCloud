import os
from django.conf import settings
from django.db import models

# Create your models here.
class Playlist(models.Model):
  genre = models.CharField(max_length = 20)
  name = models.CharField(max_length = 30)
  pub_date = models.DateTimeField('data published')
  thumbnail = models.ImageField(blank = True, upload_to = 'thumbnail/%Y/%m/%d')

  def delete(self, *args, **kargs):
        if self.thumbnail:
          os.remove(os.path.join(settings.MEDIA_ROOT, self.thumbnail.path))
          super(Playlist, self).delete(*args, **kargs)