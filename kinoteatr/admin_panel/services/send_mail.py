from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


class Mail:
    subject = 'Kinoteatr'

    def __init__(self, template, users):
        self.template = template
        self.users = users

    def sending_mail(self):
        for user in self.users:
            html_message = render_to_string(self.template.get_content_path(), {'user': user})
            # html content needs to be transformed to string to send by email protocols
            plain_message = strip_tags(html_message)  # strip tags for less smart email clients
            from_email = settings.EMAIL_HOST_USER  # set app email as a host
            to = user.email  # users emails
            send_mail(self.subject, plain_message, from_email, [to], html_message=html_message)
