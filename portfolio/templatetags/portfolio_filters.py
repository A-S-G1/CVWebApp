from django import template

register = template.Library()

@register.filter(name='split')
def split_string(value, arg):
    """
    Splits a string by the given argument (separator).
    Example: {{ value|split:"," }}
    """
    if isinstance(value, str):
        return value.split(arg)
    return value

@register.filter(name='strip')
def strip_string(value):
    """
    Strips leading and trailing whitespace from a string.
    Example: {{ value|strip }}
    """
    if isinstance(value, str):
        return value.strip()
    return value

@register.filter(name='capfirst')
def capfirst_filter(value):
    """Capitalizes the first letter of a string."""
    if isinstance(value, str):
        return value.capitalize()
    return value
