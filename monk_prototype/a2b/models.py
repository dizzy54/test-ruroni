from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class Stop(models.Model):
	id = models.CharField('stop id (eg. BEST:1234)', max_length=16, primary_key=True, unique=True)
	name = models.CharField('stop name', max_length=255)
	lat = models.FloatField()
	lon = models.FloatField()
	location = models.PointField(srid=4326, null=True)

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.location = Point(x = float(self.lon), y = float(self.lat))
		super(Stop, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = "BEST stops"