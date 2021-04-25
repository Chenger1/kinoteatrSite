from django import template

register = template.Library()


@register.filter(name='beauty_filter')
def beauty_filter(value):
    options = {
        True: 'Вкл',
        False: 'Выкл'
    }
    return options[value]


@register.filter(name='beauty_error')
def beauty_filter(value):
    text = value.replace('* ', '')
    return text


@register.filter(name='beauty_error_tag')
def beauty_filter(value):
    tags = {
        '__all__': 'Ошибка'
    }
    return tags[value]
