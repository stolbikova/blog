from django import template

register = template.Library()


@register.filter
def truncate_lines(value, num_lines):
    lines = value.splitlines()
    return '\n'.join(lines[:num_lines])
