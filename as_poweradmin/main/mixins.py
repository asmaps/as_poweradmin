# coding=utf-8

from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse


class ProfileRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, 'customerprofile'):
            messages.error(request, 'Please fill out your profile first.')
            return HttpResponseRedirect(reverse('my_profile_update'))
        return super(ProfileRequiredMixin, self).dispatch(request, *args, **kwargs)
