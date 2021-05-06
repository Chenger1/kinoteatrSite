from django import forms
from django_summernote.fields import SummernoteWidget

from cinema.models.page import Contact


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('seo', 'cinema')
        widgets = {
            'address': SummernoteWidget(attrs={'summernote': {'width': '100%'}}),
            'map': forms.Textarea(attrs={'id': 'map', 'class': 'form-control',
                                         'placeholder': '<iframe src="https://www.google.com/maps/...."></iframe>'}),
            'status': forms.CheckboxInput(attrs={'id': 'status', 'class': 'custom-control-input',
                                                 'type': 'checkbox'}),
            'top_seo': forms.CheckboxInput(attrs={'id': 'top_seo', 'class': 'custom-control-input',
                                                  'type': 'checkbox'}),
        }

    def save(self, commit=True):
        contact_inst = super().save(commit=False)
        if contact_inst.top_seo:
            prev_inst = Contact.objects.filter(top_seo=True).first()
            if prev_inst:
                prev_inst.top_seo = False
                prev_inst.save()
        if commit:
            contact_inst.save()
        return contact_inst
