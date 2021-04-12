from django.urls import path
from django.contrib.staticfiles.urls import static
from django.conf import settings

from admin_panel.views import views
from admin_panel.views import news_views
from admin_panel.views import ad_views
from admin_panel.views import movie_views
from admin_panel.views import banner_views
from admin_panel.views import cinema_views


app_name = 'admin'

urlpatterns = [
    path('index/', views.IndexAdmin.as_view(), name='admin_panel'),

    # Banners
    path('banners/', banner_views.DisplayBanner.as_view(), name='banners_admin'),
    path('banners/save_background_image/', banner_views.SaveBackgroundImage.as_view(),
         name='save_background_image'),
    path('banners/delete_background_image/', banner_views.DeleteBackgroundImage.as_view(),
         name='delete_background_image'),
    path('banners/save_on_top_banner/', banner_views.SaveOnTopBanner.as_view(),
         name='save_on_top_banner'),
    path('banners/delete_on_top_banner/<int:pk>/', banner_views.DeleteOnTopBannerGalleryImage.as_view(),
         name='delete_on_top_banner'),
    path('banners/save_slider_banner/', banner_views.SaveSliderBanner.as_view(),
         name='save_slider_banner'),
    path('banners/delete_slider_banner_image/<int:pk>/', banner_views.DeleteSliderBannerGalleryImage.as_view(),
         name='delete_slider_banner'),

    # NEWS
    path('news/', news_views.ListNews.as_view(), name='list_news_admin'),

    # ADS
    path('advertisement/', ad_views.ListAds.as_view(), name='list_ads_admin'),

    # MOVIES
    path('movies/', movie_views.ListMovies.as_view(), name='list_movie_admin'),
    path('movies/add_movie/', movie_views.AddMovie.as_view(), name='add_movie_admin'),
    path('movies/edit_movie/<int:pk>/', movie_views.UpdateMovie.as_view(), name='edit_movie_admin'),
    path('movies/delete_movie/<int:pk>/', movie_views.DeleteMovie.as_view(), name='delete_movie_admin'),
    path('movies/delete_movie_gallery_image/<int:pk>/', movie_views.DeleteMovieGalleryImage.as_view(),
         name='delete_movie_gallery_image_admin'),
    path('movies/movie_detail/<int:pk>/', movie_views.DetailMovie.as_view(), name='movie_detail_admin'),

    # CINEMA
    path('cinemas/', cinema_views.ListCinema.as_view(), name='list_cinema_admin'),
    path('cinemas/add_cinema/', cinema_views.AddCinema.as_view(), name='add_cinema_admin'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
