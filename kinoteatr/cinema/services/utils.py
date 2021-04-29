import datetime


def get_current_date():
    months = ['Января', 'Февраля', 'Марта', 'Апреля', 'Майя', 'Июня', 'Июля',
              'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря']
    current_date = datetime.date.today()
    return f'{current_date.day} {months[current_date.month-1]}'
