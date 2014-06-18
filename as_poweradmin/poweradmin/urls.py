# coding=utf-8

from django.conf.urls import patterns, include, url

from .views import DomainListView, DomainDetailView, RecordUpdateView, RecordDeleteView, RecordListJson

urlpatterns = patterns('',
    url(r'^domains/$', DomainListView.as_view(), name='domain_list'),
    url(r'^domain/(?P<pk>\d+)/$', DomainDetailView.as_view(), name='domain_detail'),
    url(r'^domain/(?P<pk>\d+).json$', RecordListJson.as_view(), name='record_list_json'),
    url(r'^record/(?P<pk>\d+)/$', RecordUpdateView.as_view(), name='record_update'),
    url(r'^record/(?P<pk>\d+)/delete/$', RecordDeleteView.as_view(), name='record_delete'),
)
