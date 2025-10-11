from django import forms
from .models import Contact, new

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

class NewForm(forms.modelForm):
    class Meta:
        model = new
        field =[ 'name', 'message']
