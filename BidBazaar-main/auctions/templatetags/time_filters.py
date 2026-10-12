from django import template
from django.utils.timesince import timesince
from datetime import datetime

register = template.Library()

@register.filter
def time_ago(value):
    if isinstance(value, datetime):
        return timesince(value) + " ago"
    return value
