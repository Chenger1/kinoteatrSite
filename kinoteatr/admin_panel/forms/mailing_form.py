from django import forms
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from cinema.models.mailing import HtmlEmail


class MailingForm(forms.Form):
    target_choices = [
        (0, 'Все пользователи'),
        (1, 'Выбранные пользователи')
    ]

    target_group = forms.ChoiceField(choices=target_choices, widget=forms.Select(attrs={'id': 'targetGroup',
                                                                                        'class': 'form-control',
                                                                                        'type': 'select'}))
    html_file = forms.FileField(required=False, widget=forms.FileInput(attrs={'type': 'file', 'id': 'htmlFile',
                                                                              'class': 'upload', 'accept': '.html',
                                                                              'required': 'true'}))
    target_users = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'id': 'targetUsers',
                                                                                             'class': 'custom-checkbox-input',
                                                                                             'type': 'checkbox'}),
                                                  queryset=get_user_model().objects.all())
    html_template = forms.ModelChoiceField(queryset=HtmlEmail.objects.all(), required=False)

    def clean(self):
        super().clean()
        if not self.cleaned_data.get('html_file') and not self.cleaned_data.get('html_template'):
            raise ValidationError('Нужно выбрать шаблон или загрузить его')

    def get_data(self):
        html_file_data = self.cleaned_data.get('html_file')
        html_template = self.cleaned_data.get('html_template')
        if html_file_data:
            html_file = HtmlEmail.objects.create(content=html_file_data)
        elif html_template:
            html_file = html_template
        else:
            raise ValidationError('Нужно выбрать шаблон или загрузить его')

        return {'html_file': html_file, 'users': self.cleaned_data['target_users']}
