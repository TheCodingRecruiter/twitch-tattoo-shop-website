from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post
from testimonial.models import Testimonial



# Create your views here.

from .models import ArtistProfile
from artwork.models import Artwork


class artistProfileListView(ListView):
    template_name = 'artistprofile/list.html'
    model = ArtistProfile

    def get_context_data(self, **kwargs):
        context = super(artistProfileListView, self).get_context_data(**kwargs)
        context['artwork'] = Artwork.objects.all()
        return context


    def get_artworkinfo(self, *args, **kwargs):
        request = self.request
        return ArtistProfile.objects.all()


class artistProfileDetailView(DetailView):
    queryset = ArtistProfile.objects.all()
    template_name = 'artistprofile/detail.html'
    model = ArtistProfile

    def get_context_data(self, **kwargs):
        context = super(artistProfileDetailView, self).get_context_data(**kwargs)
        context['artwork'] = Artwork.objects.all()
        context['blogobject'] = Post.objects.all()
        context['testimonial'] = Testimonial.objects.all()
        return context