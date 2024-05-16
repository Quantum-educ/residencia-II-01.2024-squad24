from django import template


register = template.Library()


@register.filter
def percentage(A, B):
    try:
        return f'{int(A) / int(B):.0%}'
    except (ValueError, ZeroDivisionError):
        return '0%'
