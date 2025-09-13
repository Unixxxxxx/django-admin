from django.urls import path 
from . import views

urlpatterns= [
        path('',views.index, name='index'),
        path('home/',views.home, name='home'),
        path('contact/', views.contact_view, name='contact'),
        path('', views.blog_list, name='blog_list'),
        path('<int:pk>/', views.blog_detail, name='blog_detail'),
        ]
