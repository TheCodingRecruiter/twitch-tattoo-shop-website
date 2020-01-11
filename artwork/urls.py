from django.conf.urls import url


from artwork.views import artworkListView, artworkDetailView

#Artwork

app_name = 'artwork'
urlpatterns = [
    url(r'^$', artworkListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', artworkDetailView.as_view(), name='detail'),
]