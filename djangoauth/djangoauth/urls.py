"""djangoauth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from auth.views import user_login, user_registration, dashboard, user_logout, index, base


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', base),
    url(r'^index/$', index),
    url(r'^registration/$', user_registration),
    url(r'^login/$', user_login),
    url(r'^dashboard/$', dashboard),
    url(r'^logout/$', user_logout),
]
