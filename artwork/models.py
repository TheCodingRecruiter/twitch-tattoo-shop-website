import random
import os
from django.db import models

# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1, 6546519854654)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=filename, final_filename=final_filename)    


class ArtworkQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)
    
    # def search(self, query):
    #     lookups = (Q(artist_name__icontains=query) | 
    #     Q(artwork_title__icontains=query)
    #     )
    #     return self.filter(lookups).distinct()
    

class ArtworkManager(models.Manager):
    def get_queryset(self):
        return ArtworkQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()


class Artwork(models.Model):
    artist_name = models.CharField(max_length=255)
    artwork_title = models.CharField(max_length=255, default='Artist tattoo design')
    image = models.ImageField(upload_to='artwork/', null=True, blank=True)

    objects = ArtworkQuerySet()

    
    def __str__(self):
        return self.artist_name


