from django.db import models

from albums.models import Album
# Create your models here.
class Track(models.Model):
	title = models.CharField(max_length=255)
	number = models.IntegerField()
	album_id = models.ForeignKey(Album)

	def __str__(self):
		return self.title