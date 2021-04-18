from django.db import models

import os


class HtmlEmail(models.Model):
    content = models.FileField(upload_to='htmlEmail')

    def get_content_path(self):
        return self.content.name.split('htmlEmail/')[-1]
