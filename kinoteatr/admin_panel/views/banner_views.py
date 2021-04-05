from django.shortcuts import render, redirect
from django.views.generic import View

from cinema.models.banners import BackgroundImage, OnTopBanner, SliderBanner

from admin_panel.forms.banner_form import BackgroundImageForm


class DisplayBanner(View):
    template_name = 'banner/banner_index.html'

    def get(self, request):
        background_image = BackgroundImage.load()
        on_top_banner = OnTopBanner.load()
        slider_banner = SliderBanner.load()

        return render(request, self.template_name, {'background_image': background_image,
                                                    'on_top_banner': on_top_banner,
                                                    'slider_banner': slider_banner})


class SaveBackgroundImage(View):
    model = BackgroundImage
    form = BackgroundImageForm

    def post(self, request):
        background_image_form = self.form(request.POST, request.FILES)
        if background_image_form.is_valid():
            instance = background_image_form.save(commit=False)
            status = bool(int(request.POST.get('status')))
            instance.status = status
            instance.save()

        return redirect('admin_panel:banners_admin')


class DeleteBackgroundImage(View):
    model = BackgroundImage

    def get(self, request):
        background_image = self.model.load()
        background_image.image.delete(save=True)

        return redirect('admin_panel:banners_admin')
