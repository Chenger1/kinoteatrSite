from django.db import models


class Seo(models.Model):
    seo_url = models.URLField()
    seo_title = models.CharField(max_length=100)
    seo_keywords = models.CharField(max_length=2000)
    seo_description = models.TextField(max_length=5000)

    class Meta:
        db_table = 'seo'
