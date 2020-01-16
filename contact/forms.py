from django import forms
from django.forms import ModelForm
from .models import Contact


CONTACT = (
    (0,"Appointment/Tattoo"),
    (1,"Appointment/Piercing"),
    (2,"Questions"),
    (3,"Complaints")
)


class ContactForm(ModelForm):
    customer_name = forms.CharField(max_length=255)
    customer_phone = forms.CharField(max_length=12)
    customer_email = forms.EmailField()
    contact_dropdown_options = forms.ChoiceField(choices=CONTACT, required=False)
    contact_subject = forms.CharField(max_length=255)
    contact_message = forms.CharField()
    class Meta:
        model = Contact
        fields = ['customer_name', 'customer_phone', 'customer_email', 'contact_dropdown_options', 'contact_subject', 'contact_message', 'image']
    
    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        customer_name = cleaned_data.get('customer_name')
        customer_phone = cleaned_data.get('customer_phone')
        customer_email = cleaned_data.get('customer_email')
        contact_dropdown_options = cleaned_data.get('contact_dropdown_options')
        contact_subject = cleaned_data.get('contact_subject')
        contact_message = cleaned_data.get('contact_message')
        if not customer_name and (customer_email or customer_phone) and not contact_message:
            raise forms.ValidationError('You are missing a required field')
