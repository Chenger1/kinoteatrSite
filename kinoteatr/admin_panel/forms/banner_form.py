from django import forms

from cinema.models.banners import BackgroundImage, OnTopBanner
from cinema.models.gallery import OnTopBannerGallery


class BackgroundImageForm(forms.ModelForm):
    class Meta:
        model = BackgroundImage
        fields = ('image', 'status')


class OnTopBannerForm(forms.ModelForm):
    class Meta:
        model = OnTopBanner
        fields = '__all__'


class OnTopBannerGalleryInlineForm(forms.ModelForm):
    class Meta:
        model = OnTopBannerGallery
        fields = ('image', 'url', 'text')


OnTopBannerGalleryFormSet = forms.inlineformset_factory(OnTopBanner, OnTopBannerGallery,
                                                        form=OnTopBannerGalleryInlineForm, extra=4)
