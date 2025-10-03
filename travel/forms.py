# travel/forms.py
from django import forms
from .models import QuoteRequest

class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ["full_name", "email", "phone_number", "no_of_people", "preferred_date", "message"]
        widgets = {
            "preferred_date": forms.DateInput(attrs={"type": "date"}),
            "message": forms.Textarea(attrs={"rows": 3}),
        }

