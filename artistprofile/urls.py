from django.conf.urls import url


from artistprofile.views import artistProfileListView, artistProfileDetailView

#Artwork

app_name = 'artistprofile'
urlpatterns = [
    url(r'^$', artistProfileListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', artistProfileDetailView.as_view(), name='detail'),
]