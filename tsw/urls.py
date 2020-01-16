"""tattooshopwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from accounts.views import login_page, register_page, guest_register_view

urlpatterns = [
    path('tsw-no-admin/', admin.site.urls),
    url(r'^artwork/', include('artwork.urls')),
    url(r'^artist/', include('artistprofile.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^testimonial/', include('testimonial.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^login/$', login_page, name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', register_page, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)