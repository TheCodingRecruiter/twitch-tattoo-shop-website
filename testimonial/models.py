from django.db import models

from artwork.models import Artwork

# import artistprofile.models
# Create your models here.

STATUS = (
    (0,"Not Active"),
    (1,"Active")
)

class Testimonial(models.Model):
    customer_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name="artist_artwork")
    testimony = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.customer_name