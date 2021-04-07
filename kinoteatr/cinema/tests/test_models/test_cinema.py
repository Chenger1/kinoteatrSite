from django.test import TestCase, override_settings

import tempfile

from cinema.models.seo import Seo
from cinema.models.cinema import Cinema, CinemaHall
from cinema.models.gallery import CinemaGallery, CinemaHallGallery

from test_utils.temporary_image import get_temporary_image


class TestCinema(TestCase):
    url = 'https://www.google.com/'

    @classmethod
    def setUpTestData(cls):
        cls.temp_file1 = tempfile.NamedTemporaryFile()
        cls.temp_file2 = tempfile.NamedTemporaryFile()
        cls.temp_file3 = tempfile.NamedTemporaryFile()
        cls.test_image1 = get_temporary_image(cls.temp_file1)
        cls.test_image2 = get_temporary_image(cls.temp_file2)
        cls.test_image3 = get_temporary_image(cls.temp_file3)

        cls.seo = Seo.objects.create(seo_url=cls.url, seo_title='Cinema', seo_description='Cinema1')

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_create_cinema(self):
        cinema = Cinema.objects.create(name='Cinema', description='Cinema1', conditions='Best cinema',
                                       on_top_banner=self.test_image1.name, logo=self.test_image2.name,
                                       seo=self.seo)
        image1 = CinemaGallery.objects.create(entity=cinema, image=self.test_image3.name)

        self.assertEqual(cinema.name, 'Cinema')
        self.assertEqual(image1.entity, cinema)

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_create_cinema_hall(self):
        cinema = Cinema.objects.create(name='Cinema', description='Cinema1', conditions='Best cinema',
                                       on_top_banner=self.test_image1.name, logo=self.test_image2.name, seo=self.seo)

        cinema_hall = CinemaHall.objects.create(cinema=cinema, number=1, description='CinemaHall',
                                                schema=self.test_image1.name, on_top_banner=self.test_image2.name,
                                                seo=self.seo)
        image1 = CinemaHallGallery.objects.create(entity=cinema_hall, image=self.test_image1.name)

        self.assertEqual(cinema_hall.cinema, cinema)
        self.assertIn(cinema_hall, cinema.halls.all())
        self.assertIn(image1, cinema_hall.images.all())
