from django.test import TestCase, override_settings
from django.db.utils import IntegrityError

import tempfile

from cinema.models.banners import BackgroundImage, OnTopBanner, SliderBanner
from cinema.models.gallery import OnTopBannerGallery, SliderBannerGallery

from test_utils.temporary_image import get_temporary_image


class TestBanners(TestCase):
    url = 'https://www.google.com/'

    @classmethod
    def setUpTestData(cls):
        cls.temp_file1 = tempfile.NamedTemporaryFile()
        cls.temp_file2 = tempfile.NamedTemporaryFile()
        cls.temp_file3 = tempfile.NamedTemporaryFile()
        cls.test_image1 = get_temporary_image(cls.temp_file1)
        cls.test_image2 = get_temporary_image(cls.temp_file2)
        cls.test_image3 = get_temporary_image(cls.temp_file3)

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_create_background_image(self):
        banner = BackgroundImage.objects.create(image=self.test_image1.name)
        self.assertIsNotNone(banner.image)
        self.assertEqual(len(BackgroundImage.objects.all()), 1)

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_create_slider_banner(self):
        banner = SliderBanner.objects.create(speed=0, status=True)
        image1 = SliderBannerGallery.objects.create(entity=banner, image=self.test_image1.name, url=self.url)
        image2 = SliderBannerGallery.objects.create(entity=banner, image=self.test_image2.name, url=self.url)

        self.assertEqual(len(banner.images.all()), 2)
        self.assertEqual(image1.entity, banner)
        self.assertEqual(image2.entity, banner)
        self.assertTrue(banner.status)

        self.assertEqual(banner.images.all()[0], image1)

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_create_on_top_banner(self):
        banner = OnTopBanner.objects.create(speed=1, status=True)
        image1 = OnTopBannerGallery.objects.create(entity=banner, image=self.test_image1.name, url=self.url,
                                                   text='Random Text')
        image2 = OnTopBannerGallery.objects.create(entity=banner, image=self.test_image2.name, url=self.url)

        self.assertEqual(len(banner.images.all()), 2)
        self.assertTrue(banner.status)
        self.assertEqual(banner.images.all()[0], image1)

        self.assertEqual(image1.entity, banner)
        self.assertEqual(image1.text, 'Random Text')
        self.assertEqual(image2.entity, banner)

        with self.assertRaises(IntegrityError):
            OnTopBanner.objects.create(speed=1)
