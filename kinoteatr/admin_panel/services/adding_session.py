import datetime


class Saver:
    """
    Init if user want to save multiple session.
    """
    def __init__(self, form, obj, context, request):
        self.form = form
        self.context = context
        self.request = request
        self.objects = []
        self.object = obj
        self.objects.append(self.object)
        self.date_dif = self.get_date_diff(self.object.session_datetime_start, self.request.get('end_session'))
        self.date_range = self.get_date_range()

    def get_date_diff(self, start_date: datetime, end_date: str) -> datetime.timedelta:
        """
            To save multiple session, we need to define how many days we should proceed
        """
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()  # transform string date to datetime obj
        return end_date - start_date.date()  # calculate timedelta of two dates

    def get_date_range(self) -> list:
        """
            Create list of date from first session to last.
            For example if first session start at 23.04.2021 and last session at 25.04.2021
            List will contain [23.04.2021, 24.04.2021, 25.04.2021]
        """
        date_list = [self.object.session_datetime_start + datetime.timedelta(days=x) for x in range(1, self.date_dif.days)]
        return date_list

    def save_multiple(self) -> list:
        """
            Iterate over date_range list and create new form for each date.
        """
        form_context = {
            'cinema_hall': self.object.cinema_hall,
            'movie': self.object.movie,
            'session_date': self.object.session_datetime_start,
            'session_time': self.object.session_datetime_start.time(),
            'ticket_price': self.request.get('ticket_price')
        }  # contain default context info for every session> such as cinema_hall
        for date in self.date_range:
            form_context['session_date'] = date  # different dates for each form
            form = self.form(form_context)  # but expect of that, all form have same context
            if form.is_valid():
                self.objects.append(form)  # Don`t save forms, just add them to list
                # Because if one of the form is invalid - we don`t want to save others
            else:
                raise ValueError('Ошибка в данных')
        return self.objects
