from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.

from .models import Artwork

class artworkListView(ListView):
    template_name = 'artwork/list.html'
    model = Artwork


    def get_artworkinfo(self, *args, **kwargs):
        request = self.request
        return Artwork.objects.all()


class artworkDetailView(DetailView):
    queryset = Artwork.objects.all()
    template_name = 'artwork/detail.html'


