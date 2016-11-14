from django.conf.urls import patterns, url

__author__ = 'aswathy'

urlpatterns = patterns('app_user.views',
    url(r'^$', 'index', name='index'),
)

