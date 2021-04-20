from cinema.models.movie import Movie
from cinema.models.user import User
from cinema.models.session import Session, Ticket
from cinema.models.cinema import CinemaHall


class Statistic:
    def get_movies(self):
        return Movie.objects.filter(released=True).count()

    def get_last_10_movies(self):
        return Movie.objects.all().order_by('-id')[:10]

    def get_users(self):
        return User.objects.count()

    def get_gender(self):
        return User.objects.filter(gender=0).count(), User.objects.filter(gender=1).count()

    def get_genre(self):
        result = {}
        for genre in Movie.genre_choices:
            result[genre[1]] = Movie.objects.filter(genre=genre[0]).count()
        return result

    def get_session(self):
        result = {}
        for month in range(1, 13):
            result[month] = Session.objects.filter(session_datetime_start__month=month).count()
        return result

    def get_network_load(self):
        total_seats = 0
        for hall in CinemaHall.objects.all():
            total_seats += hall.seats_amount

        bought_tickets = Ticket.objects.filter(bought=True).count()
        result = (bought_tickets*100)/total_seats
        return result
