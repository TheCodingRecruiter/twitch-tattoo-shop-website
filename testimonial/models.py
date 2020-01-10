from django.db import models

from artwork.models import Artwork


# import artistprofile.models
# Create your models here.

STATUS = (
    (0,"Not Active"),
    (1,"Active")
)


class TestimonialQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)
    
    # def search(self, query):
    #     lookups = (Q(artist_name__icontains=query) | 
    #     Q(artwork_title__icontains=query)
    #     )
    #     return self.filter(lookups).distinct()
    

class TestimonialManager(models.Manager):
    def get_queryset(self):
        return TestimonialQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()



class Testimonial(models.Model):
    customer_name = models.CharField(max_length=255)
    artist = models.CharField(default='Jason', max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name="artist_artwork")
    testimony = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    objects = TestimonialQuerySet()
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.customer_name