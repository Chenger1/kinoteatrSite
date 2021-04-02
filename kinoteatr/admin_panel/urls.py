from django.urls import path

from admin_panel.views import views
from admin_panel.views import news_views


app_name = 'admin'

urlpatterns = [
    path('index/', views.IndexAdmin.as_view(), name='admin_panel'),


    # NEWS
    path('news/', news_views.ListNews.as_view(), name='list_views_admin'),
]
