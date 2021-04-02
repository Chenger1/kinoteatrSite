from django.urls import path

from admin_panel import views

app_name = 'admin'

urlpatterns = [
    path('index/', views.IndexAdmin.as_view(), name='admin'),
]
