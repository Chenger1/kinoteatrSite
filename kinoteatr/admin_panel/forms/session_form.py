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

    class Meta:
        model = Session
        exclude = ('session_hall_schema', 'session_datetime_start', 'session_datetime_end')

    def clean(self):
        cleaned_data = super().clean()
        datetime_field_start = datetime.datetime.combine(self.cleaned_data['session_date'],
                                                         self.cleaned_data['session_time'])
        datetime_field_end = datetime_field_start + datetime.timedelta(hours=cleaned_data['movie'].running_time.hour,
                                                                       minutes=cleaned_data['movie'].running_time.minute)
        chosen_date_session = cleaned_data['cinema_hall'].sessions.filter(session_datetime_start__day=datetime_field_start.day)
        if chosen_date_session.filter(session_datetime_start__time__range=(datetime_field_start, datetime_field_end))\
                or chosen_date_session.filter(session_datetime_end__time__range=(datetime_field_start,
                                                                                 datetime_field_end)):
            str_date = datetime_field_start.strftime("%y/%m/%d, %h:%m")
            raise ValidationError(f'Сеанс на выбранную дату и время уже существует. Дата и время: {str_date}',
                                  code='Неправильное время')

        cleaned_data['datetime_field_start'] = datetime_field_start
        cleaned_data['datetime_field_end'] = datetime_field_end

    def save(self, commit=True):
        session = super().save(commit=False)

        session.session_hall_schema = session.cinema_hall.clone_schema_json()
        session.session_datetime_start = self.cleaned_data['datetime_field_start']
        session.session_datetime_end = self.cleaned_data['datetime_field_end']
        if commit:
            session.save()
        return session
