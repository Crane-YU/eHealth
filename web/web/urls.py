"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from web_design.views import homepage, send_json, send_ajax, send_data

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', homepage),
    url(r'^send_json/$', send_json),
    url(r'^send_ajax/$', send_ajax),
    url(r'^eHealth/$', send_data),
    # url(r'^post/(\w+)$', showpost),
]
