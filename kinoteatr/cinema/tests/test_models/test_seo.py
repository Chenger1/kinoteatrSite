from django.test import TestCase

from cinema.models.seo import Seo


class TestSeo(TestCase):
    url = 'https://www.google.com/'

    def test_create_seo(self):
        seo = Seo.objects.create(url=self.url, title='Title1', keywords='Keywords1, keywords2', description='Desc')

        self.assertEqual(seo.title, 'Title1')
