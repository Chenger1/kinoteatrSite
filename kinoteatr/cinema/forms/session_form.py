from django import forms


from cinema.models.session import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
