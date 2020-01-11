from django.shortcuts import render
from django.views import generic
from .models import Testimonial
from artistprofile.models import ArtistProfile
from artwork.models import Artwork

# Create your views here.


class TestimonialList(generic.ListView):
    queryset = Testimonial.objects.filter(status=1).order_by('-created_on')
    template_name = 'testimonial/list.html'
    model = Testimonial

    def get_context_data(self, **kwargs):
        context = super(TestimonialList, self).get_context_data(**kwargs)
        context['testimonial'] = Testimonial.objects.all()
        context['artist'] = ArtistProfile.objects.all()
        context['artworkobject'] = Artwork.objects.all()
        return context


class TestimonialDetail(generic.DetailView):
    model = Testimonial
    template_name = 'testimonial/testimonial_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TestimonialDetail, self).get_context_data(**kwargs)
        context['artist'] = ArtistProfile.objects.all()
        context['artwork'] = ArtistProfile.objects.all()
        return context