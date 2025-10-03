# travel/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("get-quote/", views.get_quote, name="get_quote"),
]

