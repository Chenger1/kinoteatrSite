from django.db import models
from django.dispatch import receiver

import os


@receiver(models.signals.pre_save)
def delete_old_image_after_model_update(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_image = sender.objects.get(pk=instance.pk).image
    except models.ObjectDoesNotExist:
        return False

    new_image = instance.image
    if not old_image == new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)
