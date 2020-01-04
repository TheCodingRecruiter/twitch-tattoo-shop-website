from django.contrib import admin

from .models import Artwork

# Register your models here.

class artworkAdmin(admin.ModelAdmin):
    list_display = ['artist_name', 'artwork_title']

admin.site.register(Artwork, artworkAdmin)