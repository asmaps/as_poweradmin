#!/usr/bin/python
# coding=utf-8

from django import template
from django.forms.forms import pretty_name
from django.template import defaultfilters

register = template.Library()

def render_instance_to_tr(instance, *args):
    result = ''
    fields = instance._meta.fields
    display_fields = []
    if len(args):
        for arg in args:
            display_fields.append(arg)
    elif hasattr(instance, 'get_display_field_names'):
        display_fields = instance.get_display_field_names()
    for field in fields:
        if not len(display_fields) or field.name in display_fields:
            value = unicode(getattr(instance, field.name))
            if hasattr(instance, 'get_{0}_display'.format(field.name)):
                value = getattr(instance, 'get_{0}_display'.format(field.name))()
            result += u'<tr><th class="text-right">{name}:</th><td>{value}</td></tr>'.format(
                name=unicode(pretty_name(field.verbose_name)),
                value=defaultfilters.linebreaksbr(value)
            )
    return result

register.simple_tag(render_instance_to_tr)

def render_instance_to_text(instance, *args):
    result = ''
    fields = instance._meta.fields
    display_fields = []
    if len(args):
        for arg in args:
            display_fields.append(arg)
    elif hasattr(instance, 'get_display_field_names'):
        display_fields = instance.get_display_field_names()
    for field in fields:
        if not len(display_fields) or field.name in display_fields:
            value = unicode(getattr(instance, field.name))
            if hasattr(instance, 'get_{0}_display'.format(field.name)):
                value = getattr(instance, 'get_{0}_display'.format(field.name))()
            result += u'{name}:\n{value}\n\n'.format(
                name=unicode(pretty_name(field.verbose_name)),
                value=value
            )
    return result

register.simple_tag(render_instance_to_text)

def render_dict_to_text(obj):
    result = ''
    for key,value in obj.iteritems():
        result += u'{0}: {1}\n'.format(key, value)
    return result

register.simple_tag(render_dict_to_text)
