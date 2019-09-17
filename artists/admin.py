from django.contrib import admin
from .models import Artist, Genre, Location

# Register your models here.
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Location)