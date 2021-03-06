from django.db import models


class Seo(models.Model):
    seo_url = models.URLField(blank=True)
    seo_title = models.CharField(max_length=100, blank=True)
    seo_keywords = models.CharField(max_length=2000, blank=True)
    seo_description = models.TextField(max_length=5000, blank=True)

    class Meta:
        db_table = 'seo'
