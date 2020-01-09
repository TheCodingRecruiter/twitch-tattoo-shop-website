from django.db import models
from django.contrib.auth.models import User
# Create your models here.


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class PostQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)
    
    # def search(self, query):
    #     lookups = (Q(artist_name__icontains=query) | 
    #     Q(artwork_title__icontains=query)
    #     )
    #     return self.filter(lookups).distinct()
    

class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()




class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    objects = PostQuerySet()
    
    def __str__(self):
        return self.title