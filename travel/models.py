# travel/models.py
from django.db import models

class QuoteRequest(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    no_of_people = models.IntegerField()
    preferred_date = models.DateField()
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} - {self.preferred_date}"

