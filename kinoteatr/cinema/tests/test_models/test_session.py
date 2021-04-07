from django.test import TestCase, override_settings

import tempfile

from cinema.models.session import Session, Ticket, UserTicket
from cinema.models.cinema import Cinema, CinemaHall
from cinema.models.movie import Movie
from cinema.models.user import User
from cinema.models.seo import Seo

from test_utils.temporary_image import get_temporary_image


class TestMovie(TestCase):
    url = 'https://www.google.com/'

    @classmethod
    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def setUpTestData(cls):
        cls.temp_file1 = tempfile.NamedTemporaryFile()
        cls.temp_file2 = tempfile.NamedTemporaryFile()
        cls.temp_file3 = tempfile.NamedTemporaryFile()
        cls.test_image1 = get_temporary_image(cls.temp_file1)
        cls.test_image2 = get_temporary_image(cls.temp_file2)
        cls.test_image3 = get_temporary_image(cls.temp_file3)

        cls.seo = Seo.objects.create(seo_url=cls.url, seo_title='Terminator', seo_description='Movie')
        cls.user = User.objects.create_user(email='user@mail.com', username='user1', password='secure',
                                            phone_number='123231321', gender=0)
        cls.movie = Movie.objects.create(name='Terminator', description='This is movie',
                                         main_image=cls.test_image1.name, url=cls.url,
                                         is_2d=True, status=0, release='2021-03-14', seo_id=cls.seo,
                                         language=1, director='Snyder', country='USA', genre=3, age_limit=2,
                                         running_time='1:20')

        cls.cinema = Cinema.objects.create(name='Cinema', description='Cinema1', conditions='Best cinema',
                                           on_top_banner=cls.test_image1.name, logo=cls.test_image2.name, seo=cls.seo)

        cls.cinema_hall = CinemaHall.objects.create(cinema=cls.cinema, number=1, description='CinemaHall',
                                                    schema=cls.test_image1.name, on_top_banner=cls.test_image2.name,
                                                    seo=cls.seo)

    def test_create_session(self):
        session = Session.objects.create(cinema_hall=self.cinema_hall, movie=self.movie,
                                         session_date='2021-03-12')
        tickets = []
        for _ in range(11):
            tickets.append(Ticket.objects.create(session=session, ticket_price=10,
                                                 status=True))
        user_ticket = UserTicket.objects.create(user=self.user, ticket=tickets[0])

        self.assertEqual(len(session.tickets.all()), 11)
        self.assertIn(user_ticket, self.user.tickets.all())
