from django import forms
from django.core.exceptions import ValidationError
from django_summernote.fields import SummernoteWidget

import json

from cinema.models.cinema import Cinema, CinemaHall
from cinema.models.gallery import CinemaGallery, CinemaHallGallery
from cinema.models.page import Contact


class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = ('name', 'description', 'conditions', 'on_top_banner',
                  'logo')
        widgets = {
            'name': forms.TextInput(attrs={'id': 'cinemaName', 'class': 'form-control'}),
            'description': SummernoteWidget(attrs={'summernote': {'width': '100%'}}),
            'conditions': SummernoteWidget(attrs={'summernote': {'width': '100%'}}),
            'on_top_banner': forms.FileInput(attrs={'id': 'on_top_banner', 'class': 'upload'}),
            'logo': forms.FileInput(attrs={'id': 'logo', 'class': 'upload'})
        }

    def save(self, commit=True):
        cinema_inst = super().save(commit=commit)
        if not hasattr(cinema_inst, 'contacts') and commit:
            Contact.objects.create(cinema=cinema_inst)
        return cinema_inst


class CinemaHallForm(forms.ModelForm):
    cinema = forms.ModelChoiceField(queryset=Cinema.objects.all(), widget=forms.Select(attrs={'id': 'cinema',
                                                                                              'class': 'form-control'}))

    class Meta:
        model = CinemaHall
        exclude = ('seats_amount', 'seo', 'creation_date')
        widgets = {
            'number': forms.NumberInput(attrs={'id': 'hallNumber', 'class': 'form-control'}),
            'description': SummernoteWidget(attrs={'summernote': {'width': '100%'}}),
            'on_top_banner': forms.FileInput(attrs={'id': 'on_top_banner', 'class': 'upload'}),
            'schema': forms.FileInput(attrs={'id': 'schema', 'class': 'upload'}),
            'schema_json': forms.TextInput(attrs={'id': 'schema_json', 'type': 'hidden'}),
            'is_vip_hall': forms.CheckboxInput(attrs={'id': 'isVipHall', 'class': 'form-check-input type_checkbox',
                                                      'type': 'checkbox'}),
            'is_2d': forms.CheckboxInput(attrs={'id': 'is2D', 'class': 'form-check-input type_checkbox',
                                                      'type': 'checkbox'}),
            'is_3d': forms.CheckboxInput(attrs={'id': 'is3D', 'class': 'form-check-input type_checkbox',
                                                      'type': 'checkbox'}),
            'is_imax': forms.CheckboxInput(attrs={'id': 'isImax', 'class': 'form-check-input type_checkbox',
                                                  'type': 'checkbox'}),
        }

    def clean(self):
        super().clean()
        matching = self.cleaned_data['cinema'].halls.filter(number=self.cleaned_data['number']).first()
        if matching and matching.pk != self.instance.pk:
            raise ValidationError('Кинотеатр с таким номер уже существует. Выберите другой')

    def save(self, commit=True):
        hall = super().save(commit=False)
        try:
            schema_json_raw = self.cleaned_data.get('schema_json')
            schema_json = json.loads(schema_json_raw)
            amount = self.count_seats(schema_json)
            hall.seats_amount = amount
            hall.schema_json = json.dumps(schema_json)
            if commit:
                hall.save()
            return hall
        except json.JSONDecodeError:
            raise ValidationError('В поле схемы передан неверный формат данных. Используйте конструктор.')

    def count_seats(self, schema):
        amount = 0
        for seats in schema.values():
            amount += seats.count(1)
        return amount


class CinemaGalleryForm(forms.ModelForm):
    class Meta:
        model = CinemaGallery
        fields = ('image', )
        widgets = {
            'image': forms.FileInput(attrs={'id': 'cinema_image', 'class': 'upload'})
        }


class CinemaHallGalleryForm(forms.ModelForm):
    class Meta:
        model = CinemaHallGallery
        fields = ('image', )
        widgets = {
            'image': forms.FileInput(attrs={'id': 'cinema_hall_image', 'class': 'upload'})
        }


CinemaGalleryFormSet = forms.inlineformset_factory(Cinema, CinemaGallery,
                                                   form=CinemaGalleryForm, max_num=4, extra=4, can_delete=False)

CinemaHallGalleryFormSet = forms.inlineformset_factory(CinemaHall, CinemaHallGallery,
                                                       form=CinemaHallGalleryForm, max_num=4, extra=4, can_delete=False)
