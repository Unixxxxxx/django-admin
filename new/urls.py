from django.urls import path 
from . import views

urlpatterns= [
        path('',views.index, name='index'),
        path('home/',views.home, name='home'),
        path('contact/', views.contact_view, name='contact'),
        path('menu/', views.menu, name='menu'),
        path('about/', views.about, name ='about'),
        path('form/', views.new_form_view, name='new_form'),
        path('success/', views.success_view, name='success'),
        ]
