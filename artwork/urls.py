from django.conf.urls import url


from artwork.views import artworkListView

#Artwork

app_name = 'artwork'
urlpatterns = [
    url(r'^$', artworkListView.as_view(), name='list'),
]