from django import forms
from django.core.exceptions import ValidationError

import datetime

from cinema.models.session import Session


class AddSessionForm(forms.ModelForm):
    end_session = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d', attrs={'id': 'endSession',
                                                                                   'type': 'date',
                                                                                   'class': 'form-control'}),
                                  required=False)
    session_date = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d', attrs={'id': 'sessionDate',
                                                                                    'type': 'date',
                                                                                    'class': 'form-control'}))
    session_time = forms.TimeField(widget=forms.TimeInput(attrs={'id': 'sessionTime',
                                                                 'type': 'time',
                                                                 'class': 'form-control'}))
    ticket_price = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'tickerPrice', 'type': 'number',
                                                                      'class': 'form-control', 'min': '10',
                                                                      'max': '300'}))

    class Meta:
        model = Session
        exclude = ('session_hall_schema', 'session_datetime_start', 'session_datetime_end')

        widgets = {
            'type': forms.Select(attrs={'id': 'selectType', 'class': 'form-control'})
        }

    def clean(self):
        cleaned_data = super().clean()
        datetime_field_start = datetime.datetime.combine(self.cleaned_data['session_date'],
                                                         self.cleaned_data['session_time'])
        #  Date comes in string format and, also, separated in two parts: Date and Time. So we need to combine them

        datetime_field_end = datetime_field_start + datetime.timedelta(hours=cleaned_data['movie'].running_time.hour,
                                                                       minutes=cleaned_data['movie'].running_time.minute)
        #  Using session start time and movie running time we can calculate session END time

        chosen_date_session = cleaned_data['cinema_hall'].sessions.filter(session_datetime_start__day=datetime_field_start.day)
        #  filter all sessions for the given date in purposes to be sure that there are no other sessions in this time

        if chosen_date_session.filter(session_datetime_start__range=(datetime_field_start, datetime_field_end))\
                or chosen_date_session.filter(session_datetime_end__range=(datetime_field_start,
                                                                           datetime_field_end)):
            #  if there are sessions which match with current session START time OR
            #  if there are sessions which match with current session END time
            #  We have to check not only for start or end time, but also for this range [start, end]
            #  Because if our movie starts at 12:00 PM, there can be movie that will ended in 12:30 in this hall
            #  Since we cant have two session in one hall at the same time, we have to check for this range

            str_date = datetime_field_start.strftime("%y:%m:%d, %H:%M")
            # transform date to string to place it in message
            #  If we will find another session in this time - raise Validation Error
            raise ValidationError(f'Сеанс на выбранную дату и время уже существует. Дата и время: {str_date}',
                                  code='Неправильное время')

        cleaned_data['datetime_field_start'] = datetime_field_start  # set start date
        cleaned_data['datetime_field_end'] = datetime_field_end  # set end date

    def save(self, commit=True):
        session = super().save(commit=False)

        session.session_hall_schema = session.cinema_hall.clone_schema_json()
        #  Clone cinema_hall schema. We will use it to manage tickets.
        session.session_datetime_start = self.cleaned_data['datetime_field_start']
        session.session_datetime_end = self.cleaned_data['datetime_field_end']
        if commit:
            if not session.movie.released:
                movie = session.movie
                movie.released = True  # If movie is not released - change this option because we create session
                movie.save()
            session.save()
        return session
