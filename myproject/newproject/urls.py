__author__ = 'krishnan'

from django.conf.urls import patterns, include, url
from views import archive

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    url(r'^$', archive),
)