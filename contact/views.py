from django.shortcuts import render
from django.views.generic.edit import FormView
from .models import Contact
from .forms import ContactForm

# Create your views here.

class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = '/artists/'

    def form_valid(self, form):
        return super().form_valid(form)
