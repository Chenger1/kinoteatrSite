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
from admin_panel.views import vip_hall_views
from admin_panel.views import advertisement_views
from admin_panel.views import child_room_views
from admin_panel.views import contacts_views
from admin_panel.views import user_views
from admin_panel.views import mailing_views
from admin_panel.views import session_views
from admin_panel.views import mobile_app_views

app_name = 'admin'

urlpatterns = [
    path('', views.IndexAdmin.as_view(), name='admin_panel'),
    path('login_admin/', views.LoginUserAdmin.as_view(), name='login_admin'),
    path('logout_admin/', views.LogoutAdmin.as_view(), name='logout_admin'),

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
    path('cinemas/get_session_schema/', cinema_views.GetCinemaHallSchema.as_view(), name='get_cinema_hall_schema'),

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

    # VIP HALL
    path('vip_hall/edit/', vip_hall_views.EditVipHall.as_view(), name='edit_vip_hall_admin'),
    path('vip_hall/delete_vip_hall_gallery_image/<int:pk>/', vip_hall_views.DeleteVipHallGalleryImage.as_view(),
         name='delete_vip_hall_gallery_image'),

    # ADVERTISEMENT
    path('advertisement/edit/', advertisement_views.EditAdvertisement.as_view(), name='edit_advertisement_admin'),
    path('advertisement/delete_advertisement_gallery_image/<int:pk>/',
         advertisement_views.DeleteAdvertisementGalleryImage.as_view(),
         name='delete_advertisement_gallery_image'),

    # CHILD ROOM
    path('child_room/edit/', child_room_views.EditChildRoom.as_view(), name='edit_child_room_admin'),
    path('child_room/delete_child_room_gallery_image/<int:pk>/', child_room_views.DeleteChildRoomGalleryImage.as_view(),
         name='delete_child_room_gallery_image'),

    # CONTACTS
    path('contacts/list_contacts/', contacts_views.ListContacts.as_view(), name='list_contacts_admin'),
    path('contacts/edit_contact/<int:pk>/', contacts_views.UpdateContactInfo.as_view(),
         name='edit_contact_admin'),

    # USERS
    path('user/list_users/', user_views.ListUser.as_view(), name='list_users_admin'),
    path('user/edit_user/<int:pk>/', user_views.EditUser.as_view(), name='edit_user_admin'),
    path('user/delete_user/<int:pk>/', user_views.DeleteUser.as_view(), name='delete_user_admin'),

    # MAILING
    path('mailing/mail_page/', mailing_views.DisplayMailing.as_view(), name='mailing_admin'),
    path('mailing/delete_html_template/<int:pk>/', mailing_views.DeleteHtmlEmail.as_view(),
         name='delete_html_template_admin'),

    # SESSIONS
    path('session/', session_views.DisplaySessions.as_view(),
         name='display_sessions_admin'),
    path('session/add_session/', session_views.AddSession.as_view(), name='add_session_admin'),
    path('session/detail/<int:pk>/', session_views.DetailSession.as_view(), name='detail_session_admin'),
    path('session/revert_ticket_reserving/<int:pk>/', session_views.RevertTicketReserving.as_view(),
         name='revert_ticket_reserving_admin'),
    path('session/get_cinema_hall_format/', session_views.CinemaHallFormat.as_view(), name='cinema_hall_format_session'),
    path('session/delete_session/<int:pk>/', session_views.DeleteSession.as_view(), name='delete_session'),

    # MOBILE APP
    path('mobile_app/edit/', mobile_app_views.EditMobileApp.as_view(), name='edit_mobile_app_admin'),
    path('mobile_app/delete_mobile_app_gallery_image/<int:pk>/', mobile_app_views.DeleteMobileAppGalleryImage.as_view(),
         name='delete_mobile_app_gallery_image'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
