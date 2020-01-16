import random
import os
from django.db import models

# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1, 6546519854654)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "contact/{new_filename}/{final_filename}".format(new_filename=filename, final_filename=final_filename)    


CONTACT = (
    (0,"Appointment/Tattoo"),
    (1,"Appointment/Piercing"),
    (2,"Questions"),
    (3,"Complaints")
)


class Contact(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=12)
    customer_email = models.EmailField()
    contact_dropdown_options = models.IntegerField(choices=CONTACT, default=0)
    image = models.ImageField(upload_to='contact/', null=True, blank=True)
    contact_subject = models.CharField(max_length=255)
    contact_message = models.TextField()
    
