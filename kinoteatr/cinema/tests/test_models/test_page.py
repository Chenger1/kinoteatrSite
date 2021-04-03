from django.test import TestCase, override_settings

import tempfile

from cinema.models.page import News, Ad, MainPage, AboutCinema, CafeBar, ChildRoom, Contact, VipHall, Advertisement
from cinema.models.seo import Seo
from cinema.models.cinema import Cinema
from cinema.models.gallery import NewsGallery, AdsGallery, AboutCinemaGallery, CafeBarGallery, ChildRoomGallery, \
                                  VipHallGallery, AdvertisementGallery

from cinema.tests.utils import get_temporary_image


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
        cls.cinema = Cinema.objects.create(name='Cinema', description='Cinema1', conditions='Best cinema',
                                           on_top_banner=cls.test_image1.name, logo=cls.test_image2.name,
                                           seo=cls.seo)

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_create_ad(self):
        ad = Ad.objects.create(title='Ad', description='Ad1', main_image=self.test_image1.name,
                               url=self.url, publication_date='2020-03-19', status=True, seo=self.seo)
        image1 = AdsGallery.objects.create(entity=ad, image=self.test_image2.name)
        self.assertIsNotNone(ad)
        self.assertEqual(image1.entity, ad)

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_create_news(self):
        cafebar = CafeBar.objects.create(title='Cage', description='Bar', main_image=self.test_image1.name,
                                         url=self.url, status=True, seo=self.seo)
        image1 = CafeBarGallery.objects.create(entity=cafebar, image=self.test_image2.name)
        self.assertIsNotNone(cafebar)
        self.assertEqual(image1.entity, cafebar)
        self.assertEqual(cafebar.title, cafebar.load().title)

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_create_news(self):
        vip = VipHall.objects.create(title='Vip', description='Hall', main_image=self.test_image1.name,
                                  url=self.url, status=True, seo=self.seo)
        image1 = VipHallGallery.objects.create(entity=vip, image=self.test_image2.name)
        self.assertIsNotNone(vip)
        self.assertEqual(image1.entity, vip)
        self.assertEqual(vip.title, vip.load().title)

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_create_news(self):
        ads = Advertisement.objects.create(title='Ads', description='Page', main_image=self.test_image1.name,
                                           url=self.url, status=True, seo=self.seo)
        image1 = AdvertisementGallery.objects.create(entity=ads, image=self.test_image2.name)
        self.assertIsNotNone(ads)
        self.assertEqual(image1.entity, ads)
        self.assertEqual(ads.title, ads.load().title)

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_create_news(self):
        child_room = ChildRoom.objects.create(title='Child', description='Room', main_image=self.test_image1.name,
                                              url=self.url, status=True, seo=self.seo)
        image1 = ChildRoomGallery.objects.create(entity=child_room, image=self.test_image2.name)
        self.assertIsNotNone(child_room)
        self.assertEqual(image1.entity, child_room)
        self.assertEqual(child_room.title, child_room.load().title)

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_create_news(self):
        about_cinema = AboutCinema.objects.create(title='About', description='Cinema', main_image=self.test_image1.name,
                                                  url=self.url, status=True, seo=self.seo)
        image1 = AboutCinemaGallery.objects.create(entity=about_cinema, image=self.test_image2.name)
        self.assertIsNotNone(about_cinema)
        self.assertEqual(image1.entity, about_cinema)
        self.assertEqual(about_cinema.title, about_cinema.load().title)

    def test_create_main_page(self):
        main_page = MainPage.objects.create(phone_number1='212131', phone_number2='121323',
                                            status=True, seo=self.seo)
        self.assertIsNotNone(main_page)
        self.assertEqual(main_page.phone_number1, main_page.load().phone_number1)

    def test_create_contacts(self):
        contacts = Contact.objects.create(cinema=self.cinema, address='Street',
                                          coord_x=12, coord_y=44, seo=self.seo)

        self.assertIsNotNone(contacts)
        self.assertEqual(contacts.cinema, contacts.load().cinema)
