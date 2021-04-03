from django.urls import path

from admin_panel.views import views
from admin_panel.views import news_views
from admin_panel.views import ad_views
from admin_panel.views import movie_views


app_name = 'admin'

urlpatterns = [
    path('index/', views.IndexAdmin.as_view(), name='admin_panel'),


    # NEWS
    path('news/', news_views.ListNews.as_view(), name='list_news_admin'),

    # ADS
    path('advertisement/', ad_views.ListAds.as_view(), name='list_ads_admin'),

    # MOVIES
    path('movies/', movie_views.ListMovies.as_view(), name='list_movie_admin'),
]
