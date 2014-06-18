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

from .mixins import ProfileRequiredMixin
from .forms import UserNameForm
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

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['nav_home'] = True
        return context


class MyProfileView(LoginRequiredMixin, ProfileRequiredMixin, TemplateView):
    template_name = 'main/my_profile.html'

    def get_context_data(self, **kwargs):
        context = super(MyProfileView, self).get_context_data(**kwargs)
        context['nav_my_profile'] = True
        return context


class MyProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomerProfile
    template_name = 'main/my_profile_update.html'
    fields = []

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Successfully updated your profile information.')
        return reverse('my_profile')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            self.username_form = UserNameForm(instance=self.request.user)
        return super(MyProfileUpdateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.username_form = UserNameForm(self.request.POST, instance=self.request.user)
        if self.username_form.is_valid():
            self.username_form.save()
        else:
            return self.form_invalid(form)
        return super(MyProfileUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        self.username_form = UserNameForm(self.request.POST, instance=self.request.user)
        # validate form to get error messages
        self.username_form.is_valid()
        return super(MyProfileUpdateView, self).form_invalid(form)

    def get_object(self, queryset=None):
        if hasattr(self.request.user, 'customerprofile'):
            return self.request.user.customerprofile
        else:
            return CustomerProfile(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(MyProfileUpdateView, self).get_context_data(**kwargs)
        helper = FormHelper()
        helper.form_tag = False
        helper.add_input(Submit('submit', 'Save', css_class='btn btn-primary pull-right'))
        context['form'].helper = helper
        context['username_form'] = self.username_form
        context['nav_my_profile'] = True
        return context

