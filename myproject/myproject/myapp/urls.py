# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('myproject.myapp.views',
    url(r'^upload/$', 'list', name='list'),
    url(r'^plot/$', 'makeGraph', name='makeGraph'),
    #url(r'^plot/$', 'plot', name='plot'),
)
