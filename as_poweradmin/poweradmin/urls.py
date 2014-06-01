# coding=utf-8

from django.conf.urls import patterns, include, url

from .views import DomainListView

urlpatterns = patterns('',
    url(r'^domains/$', DomainListView.as_view(), name='domain_list'),
)
