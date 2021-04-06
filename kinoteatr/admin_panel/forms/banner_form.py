from django import forms

from cinema.models.banners import BackgroundImage, OnTopBanner, SliderBanner
from cinema.models.gallery import OnTopBannerGallery, SliderBannerGallery


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
                                                        form=OnTopBannerGalleryInlineForm, extra=4, max_num=8)


class SliderBannerForm(forms.ModelForm):
    class Meta:
        model = SliderBanner
        fields = '__all__'


class SliderBannerGalleryInlineForm(forms.ModelForm):
    class Meta:
        model = SliderBannerGallery
        fields = ('image', 'url')


SliderBannerGalleryFormSet = forms.inlineformset_factory(SliderBanner, SliderBannerGallery,
                                                         form=SliderBannerGalleryInlineForm, extra=4, max_num=8)
