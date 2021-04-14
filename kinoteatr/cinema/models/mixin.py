from django.db import models

from cinema.models.seo import Seo


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        if not obj.seo:
            obj.seo = Seo.objects.create()
            obj.save()
        return obj
