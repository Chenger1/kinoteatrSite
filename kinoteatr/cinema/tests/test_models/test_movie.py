from django.test import TestCase, override_settings

import tempfile

from cinema.models.movie import Movie, ExtendedInfo
from cinema.models.seo import Seo
from cinema.models.gallery import MovieGallery

from test_utils.temporary_image import get_temporary_image


class TestMovie(TestCase):
    url = 'https://www.google.com/'

    @classmethod
    def setUpTestData(cls):
        cls.temp_file1 = tempfile.NamedTemporaryFile()
        cls.temp_file2 = tempfile.NamedTemporaryFile()
        cls.temp_file3 = tempfile.NamedTemporaryFile()
        cls.test_image1 = get_temporary_image(cls.temp_file1)
        cls.test_image2 = get_temporary_image(cls.temp_file2)
        cls.test_image3 = get_temporary_image(cls.temp_file3)

        cls.seo = Seo.objects.create(url=cls.url, title='Terminator', description='Movie')

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_create_movie(self):
        movie = Movie.objects.create(name='Terminator', description='This is movie',
                                     main_image=self.test_image1.name, url=self.url,
                                     is_2d=True, status=0, release='2021-03-14', seo_id=self.seo)
        extended_info = ExtendedInfo(movie=movie, language=1, director='Snyder', country='USA',
                                     genre=3, age_limit=2)

        image1 = MovieGallery.objects.create(entity=movie, image=self.test_image2.name)
        image2 = MovieGallery.objects.create(entity=movie, image=self.test_image3.name)

        self.assertEqual(movie.info, extended_info)
        self.assertEqual(len(movie.images.all()), 2)
        self.assertEqual(image1.entity, movie)
        self.assertIn(movie, self.seo.movies.all())
