# coding=utf-8
from django.views.generic import (
    TemplateView, DetailView, ListView, UpdateView
)
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect

from allauth.account.views import LoginView, SignupView, PasswordChangeView
from braces.views import LoginRequiredMixin
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


from .models import CustomerProfile


class CrispyLoginView(LoginView):
    def get_context_data(self, **kwargs):
        context = super(CrispyLoginView, self).get_context_data(**kwargs)
        helper = FormHelper()
        helper.form_tag = False
        context['crispy_helper'] = helper
        return context


class CrispySignupView(SignupView):
    def get_context_data(self, **kwargs):
        context = super(CrispySignupView, self).get_context_data(**kwargs)
        helper = FormHelper()
        helper.form_tag = False
        context['crispy_helper'] = helper
        return context


class CrispyPasswordChangeView(PasswordChangeView):
    def get_context_data(self, **kwargs):
        context = super(CrispyPasswordChangeView, self).get_context_data(**kwargs)
        helper = FormHelper()
        helper.form_tag = False
        context['crispy_helper'] = helper
        return context


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'main/home.html'


class MyProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'main/my_profile.html'
    model = CustomerProfile

    def get_object(self):
        return None
