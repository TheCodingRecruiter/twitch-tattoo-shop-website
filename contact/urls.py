from django.conf.urls import url


from .views import ContactView

#Artwork

app_name = 'contact'
urlpatterns = [
    url(r'^$', ContactView.as_view(), name='contact'),
]