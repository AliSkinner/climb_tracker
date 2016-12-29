from django.contrib import admin
from .models import Route, Area, Location, Session

admin.site.register(Location)
admin.site.register(Area)
admin.site.register(Route)
admin.site.register(Session)
