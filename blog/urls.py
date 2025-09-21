from django.urls import path
from . import views

urlpatterns =[
        path('',views.blog, name='blog'),
        #path("chatbot/", views.chatbot_response, name="chatbot"),
        path("chatbot/", views.chatbot_response, name="chatbot_response"),
        ]
