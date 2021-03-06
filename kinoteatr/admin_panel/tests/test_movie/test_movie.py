from django.test import TestCase, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile

import tempfile


from admin_panel.forms.movie_form import MovieForm

from test_utils.temporary_image import get_temporary_bytes_io_image


class TestMovie(TestCase):
    data = {
        'name': 'Movie',
        'description': 'Movie desc',
        'url': 'https://google.com',
        'is_2d': True,
        'is_3d': False,
        'is_imax': False,
        'status': 1,
        'release': '2020-02-02',
    }
    extended_info = {
        'language': 1,
        'director': 'Snider',
        'running_time': '12:10:03',
        'country': 'Ukraine',
        'genre': 1,
        'age_limit': 1
    }

    @classmethod
    def setUpTestData(cls):
        cls.temp_file = tempfile.NamedTemporaryFile()
        cls.test_image1 = get_temporary_bytes_io_image()
        cls.test_image2 = get_temporary_bytes_io_image()
        cls.test_image3 = get_temporary_bytes_io_image()

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_movie_form(self):
        files = {
            'main_image': SimpleUploadedFile(name='main_image.png', content=self.test_image1.read(),
                                             content_type='image/png')
        }
        form = MovieForm(data=self.data, files=files)
        self.assertTrue(form.is_valid())

    def test_error_movie(self):
        data = {
            'is_2d': True,
            'is_3d': False,
            'is_imax': False,
            'status': 1,
            'release': '2020-02-02',
        }
        files = {
            'main_image': SimpleUploadedFile(name='main_image.png', content=self.test_image2.read(),
                                             content_type='image/png')
        }
        form = MovieForm(data=data, files=files)
        self.assertFalse(form.is_valid())
