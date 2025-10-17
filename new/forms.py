from django import forms
from .models import Contact,new, alpha 

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

class NewForm(forms.ModelForm):
    class Meta:
        model = new
        fields =[ 'name', 'message']

class Newalpha(forms.ModelForm):
    class Meta:
        model = alpha
        fields = ['name', 'email']
