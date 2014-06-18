# coding=utf-8
from braces.views import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import ListView, UpdateView, DeleteView, View
from powerdns_manager.models import Domain, Record


class DomainListView(LoginRequiredMixin, ListView):
    template_name = 'poweradmin/domain_list.html'

    def get_queryset(self):
        return Domain.objects.filter(created_by=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(DomainListView, self).get_context_data(**kwargs)
        context['nav_domains'] = True
        return context


class DomainDetailView(LoginRequiredMixin, ListView):
    template_name = 'poweradmin/domain_detail.html'
    model = Record

    def get_queryset(self):
        self.domain = Domain.objects.get(pk=self.kwargs['pk'])
        if not self.domain.created_by == self.request.user:
            raise PermissionDenied()
        records = self.domain.powerdns_manager_record_domain.all()
        return records

    def get_context_data(self, **kwargs):
        context = super(DomainDetailView, self).get_context_data(**kwargs)
        context['domain'] = self.domain
        return context


class RecordListJson(LoginRequiredMixin, View):

    def get_queryset(self):
        self.domain = Domain.objects.get(pk=self.kwargs['pk'])
        if not self.domain.created_by == self.request.user:
            raise PermissionDenied()
        records = self.domain.powerdns_manager_record_domain.all()
        return records

    def get(self, request, *args, **kwargs):
        json = render_to_string('poweradmin/record_list.json',
                                {'record_list': self.get_queryset()})
        return HttpResponse(json)


class RecordUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'poweradmin/record_update.html'
    model = Record
    fields = ['name', 'type', 'content', 'prio']

    def get_object(self, queryset=None):
        obj = super(RecordUpdateView, self).get_object(queryset)
        if not obj.domain.created_by == self.request.user:
            raise PermissionDenied()
        return obj


class RecordDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'poweradmin/record_confirm_delete.html'
    model = Record

    def get_success_url(self):
        return reverse('domain_detail', kwargs={'pk': self.object.domain.pk})

    def get_object(self, queryset=None):
        obj = super(RecordDeleteView, self).get_object(queryset)
        if not obj.domain.created_by == self.request.user:
            raise PermissionDenied()
        return obj
