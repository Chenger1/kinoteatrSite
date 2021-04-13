from django import forms
from django_summernote.fields import SummernoteWidget

from cinema.models.page import News
from cinema.models.gallery import NewsGallery


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ('seo',)
        widgets = {
            'title': forms.TextInput(attrs={'id': 'newsName', 'class': 'form-control'}),
            'description': SummernoteWidget(attrs={'summernote': {'width': '100%'}}),
            'main_image': forms.FileInput(attrs={'id': 'main_image', 'class': 'upload'}),
            'url': forms.URLInput(attrs={'id': 'url', 'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'id': 'status', 'class': 'custom-control-input',
                                                 'type': 'checkbox'}),
            'publication_date': forms.DateInput(format='%Y-%m-%d', attrs={'id': 'newsPublicationDate',
                                                                          'type': 'date',
                                                                          'class': 'form-control'})
        }


class NewsGalleryForm(forms.ModelForm):
    class Meta:
        model = NewsGallery
        fields = ('image', )
        widgets = {
            'image': forms.FileInput(attrs={'id': 'gallery_image', 'class': 'upload'})
        }


NewsGalleryFormSet = forms.inlineformset_factory(News, NewsGallery,
                                                 form=NewsGalleryForm, max_num=4, extra=4, can_delete=False)
