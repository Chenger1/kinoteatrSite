from django.db import models


class Seo(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=2000)
    description = models.TextField(max_length=5000)

    class Meta:
        db_table = 'seo'
