
from django.conf.urls import url


from .views import ProductListView, ProductDetailSlugView

app_name = 'products'
urlpatterns = [    
    url(r'^$', ProductListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
]