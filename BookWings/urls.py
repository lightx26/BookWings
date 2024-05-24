"""
URL configuration for BookWings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from .views import index, about

from django.urls import re_path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', index, name='home'),
    path('home/', index, name='home'),
    path('about/', about, name='about'),
    path('', include('accounts.urls')),
    path('books/', include('books.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('delivery/', include('delivery.urls')),
    # your other paths here
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
]
