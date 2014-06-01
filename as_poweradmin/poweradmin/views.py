# coding=utf-8
from django.views.generic import (
    TemplateView, DetailView, ListView
)
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect

from braces.views import LoginRequiredMixin

from powerdns_manager.models import Domain


class DomainListView(LoginRequiredMixin, ListView):
    template_name = 'poweradmin/domain_list.html'

    def get_queryset(self):
        return Domain.objects.filter(created_by=self.request.user)
