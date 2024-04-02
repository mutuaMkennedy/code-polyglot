from django.contrib.gis import admin
from .models import Route, Station

admin.site.register(Route, admin.GISModelAdmin)
admin.site.register(Station, admin.GISModelAdmin)
