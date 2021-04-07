from django.test import TestCase

from cinema.models.seo import Seo


class TestSeo(TestCase):
    url = 'https://www.google.com/'

    def test_create_seo(self):
        seo = Seo.objects.create(seo_url=self.url, seo_title='Title1', seo_keywords='Keywords1, keywords2',
                                 seo_description='Desc')

        self.assertEqual(seo.seo_title, 'Title1')
