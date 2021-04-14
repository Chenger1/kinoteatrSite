from django.urls import path
from django.contrib.staticfiles.urls import static
from django.conf import settings

from admin_panel.views import views
from admin_panel.views import news_views
from admin_panel.views import ad_views
from admin_panel.views import movie_views
from admin_panel.views import banner_views
from admin_panel.views import cinema_views
from admin_panel.views import main_page_views
from admin_panel.views import about_cinema_views
from admin_panel.views import cafe_bar_views


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
    path('news/add_news/', news_views.AddNews.as_view(), name='add_news_admin'),
    path('news/edit_news/<int:pk>/', news_views.UpdateNews.as_view(), name='edit_news_admin'),
    path('news/delete_news/<int:pk>/', news_views.DeleteNews.as_view(), name='delete_news_admin'),
    path('news/delete_news_gallery_image/<int:pk>/', news_views.DeleteNewsGalleryImage.as_view(),
         name='delete_news_gallery_image_admin'),

    # ADS
    path('ads/', ad_views.ListAds.as_view(), name='list_ads_admin'),
    path('ads/add_new_ad/', ad_views.AddAd.as_view(), name='add_ad_admin'),
    path('ads/edit_ad/<int:pk>/', ad_views.UpdateAd.as_view(), name='edit_ad_admin'),
    path('ads/delete_ad/<int:pk>/', ad_views.DeleteAd.as_view(), name='delete_ad_admin'),
    path('ads/delete_ad_gallery_image/<int:pk>/', ad_views.DeleteAdGalleryImage.as_view(),
         name='delete_ad_gallery_image_admin'),

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
    path('cinemas/edit_cinema/<int:pk>/', cinema_views.UpdateCinema.as_view(),
         name='edit_cinema_admin'),
    path('cinemas/delete_cinema/<int:pk>/', cinema_views.DeleteCinema.as_view(),
         name='delete_cinema_admin'),
    path('cinemas/delete_cinema_gallery_image/<int:pk>/', cinema_views.DeleteCinemaGalleryImage.as_view(),
         name='delete_cinema_gallery_image'),

    # # Cinema Hall
    path('cinemas/add_cinema_hall/<int:pk>/', cinema_views.AddCinemaHall.as_view(),
         name='add_cinema_hall'),
    path('cinemas/edit_cinema_hall/<int:pk>/', cinema_views.UpdateCinemaHall.as_view(),
         name='edit_cinema_hall'),
    path('cinemas/delete_cinema_hall/<int:pk>/', cinema_views.DeleteCinemaHall.as_view(),
         name='delete_cinema_hall'),
    path('cinemas/delete_cinema_hall_gallery_image/<int:pk>/', cinema_views.DeleteCinemaHallGalleryImage.as_view(),
         name='delete_cinema_hall_gallery_image'),

    # MAIN PAGE
    path('main_page/edit/', main_page_views.EditMainPage.as_view(), name='edit_main_page_admin'),

    # ABOUT CINEMA
    path('about_cinema/edit/', about_cinema_views.EditAboutCinema.as_view(), name='edit_about_cinema_admin'),
    path('about_cinema/delete_about_cinema_gallery_image/<int:pk>/', about_cinema_views.DeleteAboutCinemaGalleryImage.as_view(),
         name='delete_about_cinema_gallery_image'),

    # CAFE BAR
    path('cafe_bar/edit/', cafe_bar_views.EditCafeBar.as_view(), name='edit_cafe_bar_admin'),
    path('cafe_bar/delete_cafe_bar_gallery_image/<int:pk>/', cafe_bar_views.DeleteCafeBarGalleryImage.as_view(),
         name='delete_cafe_bar_gallery_image'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
