from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import get_user_model

from cinema.models.mailing import HtmlEmail

from admin_panel.forms.mailing_form import MailingForm
from admin_panel.services.send_mail import Mail


User = get_user_model()


class DisplayMailing(View):
    template_name = 'mailing/mail.html'
    form = MailingForm

    def get(self, request):
        form = self.form()
        context = self.get_context_data(form)
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST, request.FILES)
        if form.is_valid():
            data = form.get_data()
            mail_obj = Mail(data['html_file'], data['users'])
            mail_obj.sending_mail()

        context = self.get_context_data(form)
        return render(request, self.template_name, context)

    def get_context_data(self, form):
        user_amount = User.objects.count()
        users = User.objects.all()
        mail_templates = HtmlEmail.objects.all().reverse()[:5]
        return {'users': users,
                'user_amount': user_amount,
                'mail_templates': mail_templates,
                'form': form}
