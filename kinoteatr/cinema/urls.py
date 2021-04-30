from django.urls import path
from django.contrib.staticfiles.urls import static
from django.conf import settings

from cinema.views.views import DisplayMainPage, ListMovies, MovieDetail, MovieSessionDetail
from cinema.views.pages.news_views import ListNews, NewsDetail

app_name = 'cinema'


urlpatterns = [
    path('', DisplayMainPage.as_view(), name='main_page'),
    path('show_movies_list/', ListMovies.as_view(), name='show_list_movies'),
    path('movie_detail/<int:pk>/', MovieDetail.as_view(), name='movie_detail'),
    path('movie_detail/sessions', MovieSessionDetail.as_view(), name='movie_sessions'),

    # NEWS
    path('news/', ListNews.as_view(), name='list_news'),
    path('news/detail/<int:pk>/', NewsDetail.as_view(), name='public_news_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
