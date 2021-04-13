from django import template

register = template.Library()


@register.filter(name='beauty_filter')
def beauty_filter(value):
    options = {
        True: 'Вкл',
        False: 'Выкл'
    }
    return options[value]
