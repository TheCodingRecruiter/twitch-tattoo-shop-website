from django.db import models
from artwork.models import Artwork
from blog.models import Post
from testimonial.models import Testimonial
from django.urls import reverse

# Create your models here.


class ArtistProfileQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)
    

class ArtistProfileManager(models.Manager):
    def get_queryset(self):
        return ArtistProfileQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()


class ArtistProfile(models.Model):
    artist = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12)
    artwork = models.ManyToManyField(Artwork, blank=True)
    tattoo_artist = models.BooleanField(default=True)
    piercing_artist = models.BooleanField(default=False)
    blog_posts = models.ManyToManyField(Post, blank=True)
    customer_testimonials = models.ManyToManyField(Testimonial, blank=True)

    objects = ArtistProfileQuerySet()

    def __str__(self):
        return self.artist
