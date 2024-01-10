from django import template

register = template.Library()

@register.filter
def bar_color(value):
    if value < 50:
        return 'bg-danger'
    elif value < 100:
        return 'bg-warning'
    else:
        return 'bg-success'
