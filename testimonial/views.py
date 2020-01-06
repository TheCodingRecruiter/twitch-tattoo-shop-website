from django.shortcuts import render
from django.views import generic
from .models import Testimonial

# Create your views here.


class TestimonialList(generic.ListView):
    queryset = Testimonial.objects.filter(status=1).order_by('-created_on')
    template_name = 'testimonial/list.html'

class TestimonialDetail(generic.DetailView):
    model = Testimonial
    template_name = 'testimonial/testimonial_detail.html'