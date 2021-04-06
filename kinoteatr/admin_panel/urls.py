from django.urls import path
from django.contrib.staticfiles.urls import static
from django.conf import settings

from admin_panel.views import views
from admin_panel.views import news_views
from admin_panel.views import ad_views
from admin_panel.views import movie_views
from admin_panel.views import banner_views


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

    # NEWS
    path('news/', news_views.ListNews.as_view(), name='list_news_admin'),

    # ADS
    path('advertisement/', ad_views.ListAds.as_view(), name='list_ads_admin'),

    # MOVIES
    path('movies/', movie_views.ListMovies.as_view(), name='list_movie_admin'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
