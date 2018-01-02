from django import template

register = template.Library()

@register.simple_tag
def format_dates(start, end):
    pass
