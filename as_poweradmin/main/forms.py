# coding=utf-8

from django import forms
from django.contrib.auth import get_user_model
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import InlineField
from crispy_forms.helper import FormHelper


class UserNameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserNameForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name']
