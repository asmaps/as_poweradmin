# coding=utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

from model_utils.models import TimeStampedModel


class CustomerProfile(TimeStampedModel):
    user = models.OneToOneField(get_user_model())
