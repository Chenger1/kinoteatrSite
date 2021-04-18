from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class Mail:
    subject = 'Kinoteatr'

    def __init__(self, template, users):
        self.template = template
        self.users = users

    def sending_mail(self):
        for user in self.users:
            html_message = render_to_string(self.template.get_content_path(), {'user': user})
            plain_message = strip_tags(html_message)
            from_email = 'kinoteatr@gmail.com'
            to = user.email
            send_mail(self.subject, plain_message, from_email, [to], html_message=html_message)
