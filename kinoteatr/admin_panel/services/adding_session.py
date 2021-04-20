import datetime


class Saver:
    def __init__(self, form, obj, context, request):
        self.form = form
        self.context = context
        self.request = request
        self.objects = []
        self.object = obj
        self.objects.append(self.object)
        self.date_dif = self.get_date_diff(self.object.session_datetime_start, self.request.get('end_session'))
        self.date_range = self.get_date_range()

    def get_date_diff(self, start_date: datetime, end_date: str):
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
        return end_date - start_date.date()

    def get_date_range(self):
        date_list = [self.object.session_datetime_start + datetime.timedelta(days=x) for x in range(1, self.date_dif.days)]
        return date_list

    def save_multiple(self):
        form_context = {
            'cinema_hall': self.object.cinema_hall,
            'movie': self.object.movie,
            'session_date': self.object.session_datetime_start,
            'session_time': self.object.session_datetime_start.time(),
            'ticket_price': self.request.get('ticket_price')
        }
        for date in self.date_range:
            form_context['session_date'] = date
            form = self.form(form_context)
            if form.is_valid():
                self.objects.append(form)
            else:
                raise ValueError('Ошибка в данных')
        return self.objects
