__author__ = 'krishnan'

from django.conf.urls import patterns, include, url
from views import archive, get_article, blog_home

urlpatterns = patterns('',
    url(r'^$', blog_home, name='home'),
    url(r'^(?P<id>\d+)/$', get_article, name='article'),
    url(r'^archive/$', archive, name='archive'),
)
