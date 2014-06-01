#!/usr/bin/python
# coding=utf-8


def get_user_display(user):
    if user.first_name and user.last_name:
        return u'{user.first_name} {user.last_name}'.format(user=user)
    return user.email
