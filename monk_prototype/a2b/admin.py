from django.contrib.gis import admin
from models import Stop
#from django.contrib.gis.geos import Point

class StopAdmin(admin.OSMGeoAdmin):
	fields = ('name', 'id', 'lat', 'lon', 'location')
	#readonly_fields = ('location',)

	#def location(self, obj):
	#	return Point(x = obj.lat, y = obj.lon)


admin.site.register(Stop,StopAdmin)

# Register your models here.
