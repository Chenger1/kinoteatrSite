from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from cinema.models.banners import BackgroundImage, OnTopBanner, SliderBanner
from cinema.models.gallery import OnTopBannerGallery, SliderBannerGallery

from admin_panel.forms.banner_form import BackgroundImageForm, OnTopBannerForm, OnTopBannerGalleryFormSet,\
                                          SliderBannerGalleryFormSet, SliderBannerForm

from admin_panel.utils.messages import beautify_error_messages


class DisplayBanner(View):
    template_name = 'banner/banner_index.html'

    def get(self, request):
        background_image = BackgroundImage.load()
        on_top_banner = OnTopBanner.load()
        slider_banner = SliderBanner.load()

        on_top_banner_form = OnTopBannerForm()
        on_top_banner_gallery_form_set = OnTopBannerGalleryFormSet(instance=on_top_banner, prefix='on_top')

        slider_banner_form = SliderBannerForm()
        slider_banner_form_set = SliderBannerGalleryFormSet(instance=slider_banner, prefix='slider')

        return render(request, self.template_name, {'background_image': background_image,
                                                    'on_top_banner': on_top_banner,
                                                    'on_top_banner_form': on_top_banner_form,
                                                    'on_top_banner_form_set': on_top_banner_gallery_form_set,
                                                    'slider_banner': slider_banner,
                                                    'slider_banner_form': slider_banner_form,
                                                    'slider_banner_form_set': slider_banner_form_set})


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
        else:
            beautify_error_messages(background_image_form.errors, request)

        return redirect('admin_panel:banners_admin')


class DeleteBackgroundImage(View):
    model = BackgroundImage

    def get(self, request):
        background_image = self.model.load()
        background_image.image.delete(save=True)

        return redirect('admin_panel:banners_admin')


class SaveOnTopBanner(View):
    model = OnTopBanner
    inline_model = OnTopBannerGallery
    form = OnTopBannerForm
    inline_form = OnTopBannerGalleryFormSet

    def post(self, request):
        on_top_banner = self.model.load()
        form = self.form(request.POST, instance=on_top_banner)
        inline_form = self.inline_form(request.POST, request.FILES, prefix='on_top', instance=on_top_banner)

        if form.is_valid():
            form.save()
            if inline_form.is_valid():
                inline_form.save()
            else:
                beautify_error_messages(inline_form.errors, request)
        else:
            beautify_error_messages(form.errors, request)

        return redirect('admin_panel:banners_admin')


class DeleteOnTopBannerGalleryImage(View):
    model = OnTopBannerGallery

    def get(self, request, pk):
        inst = get_object_or_404(self.model, pk=pk)
        inst.image.delete()
        inst.delete()

        return redirect('admin_panel:banners_admin')


class SaveSliderBanner(View):
    model = SliderBanner
    inline_model = SliderBannerGallery
    form = SliderBannerForm
    inline_form = SliderBannerGalleryFormSet

    def post(self, request):
        slider_banner = self.model.load()
        form = self.form(request.POST, instance=slider_banner)
        inline_form = self.inline_form(request.POST, request.FILES, prefix='slider', instance=slider_banner)

        if form.is_valid():
            form.save()
            if inline_form.is_valid():
                inline_form.save()
            else:
                beautify_error_messages(inline_form.errors, request)
        else:
            beautify_error_messages(form.errors, request)

        return redirect('admin_panel:banners_admin')


class DeleteSliderBannerGalleryImage(View):
    model = SliderBannerGallery

    def get(self, request, pk):
        inst = get_object_or_404(self.model, pk=pk)
        inst.image.delete()
        inst.delete()

        return redirect('admin_panel:banners_admin')
