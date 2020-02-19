from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),# '' -> home page
    path('about/', views.about, name='blog-about'),
    ]
