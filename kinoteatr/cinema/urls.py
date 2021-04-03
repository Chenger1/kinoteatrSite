from django.urls import path
from django.contrib.staticfiles.urls import static
from django.conf import settings


app_name = 'cinema'


urlpatterns = [

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
