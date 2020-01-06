from django.urls import path

from .views import TestimonialList, TestimonialDetail

app_name = 'testimonial'
urlpatterns = [
    path('', TestimonialList.as_view(), name='list'),
    path('<slug:slug>/', TestimonialDetail.as_view(), name='testimonial_detail'),
]