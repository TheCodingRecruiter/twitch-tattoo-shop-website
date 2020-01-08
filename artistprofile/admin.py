from django.contrib import admin

from .models import ArtistProfile
# Register your models here.

class artistAdmin(admin.ModelAdmin):
    list_display = ['artist', 'email', 'phone', 'tattoo_artist', 'piercing_artist']

admin.site.register(ArtistProfile, artistAdmin)