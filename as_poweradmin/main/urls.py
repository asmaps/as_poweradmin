# coding=utf-8

from django.conf.urls import patterns, include, url

from .views import (
    HomeView, MyProfileView, MyProfileUpdateView,
    CrispyLoginView, CrispyPasswordChangeView, CrispySignupView,
)

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^my_profile/$', MyProfileView.as_view(), name='my_profile'),
    url(r'^my_profile/update/$', MyProfileUpdateView.as_view(), name='my_profile_update'),
    url(r'^accounts/login/$', CrispyLoginView.as_view(), name='account_login'),
    url(r'^accounts/signup/$', CrispySignupView.as_view(), name='account_signup'),
    url(r'^accounts/password/change/$', CrispyPasswordChangeView.as_view(), name='account_change_password'),
)
