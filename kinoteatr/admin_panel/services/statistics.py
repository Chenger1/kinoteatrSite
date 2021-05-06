from cinema.models.movie import Movie
from cinema.models.user import User
from cinema.models.session import Session, Ticket
from cinema.models.cinema import CinemaHall

from typing import List, Tuple, Dict


class Statistic:
    def get_movies(self) -> List[Movie]:  # BUT, it is a QuerySet type
        return Movie.objects.filter(released=True).count()  # counts only released movies

    def get_last_10_movies(self) -> List[Movie]:  # BUT, it is a QuerySet type
        return Movie.objects.all().order_by('-id')[:5]

    def get_users(self) -> int:
        return User.objects.count()

    def get_gender(self) -> Tuple[int, int]:
        return User.objects.filter(gender=0).count(), User.objects.filter(gender=1).count()

    def get_genre(self) -> Dict[str, int]:
        """
            counts movies by each genre
        """
        result = {}
        for genre in Movie.genre_choices:
            result[genre[1]] = Movie.objects.filter(genre=genre[0]).count()
        return result

    def get_session(self) -> Dict[str, int]:
        """
        Count session my month
        """
        result = {}
        for month in range(1, 13):
            result[month] = Session.objects.filter(session_datetime_start__month=month).count()
        return result

    def get_network_load(self):
        """
        Calculate how hard cinema network works
        """
        total_seats = 0
        for hall in CinemaHall.objects.all():
            total_seats += hall.seats_amount  # total number of seats

        bought_tickets = Ticket.objects.filter(bought=True).count()  # how many tickets bought
        try:
            result = (bought_tickets*100)/total_seats
        except ZeroDivisionError:
            result = 0
        return round(result, 2)
