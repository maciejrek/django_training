"""
Definition of urls for DjangoTraining.
"""

from datetime import datetime
from django.urls import path, include 
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from users import views as user_views


urlpatterns = [
    #path('', views.home, name='home'),
    #path('contact/', views.contact, name='contact'),
    #path('about/', views.about, name='about'),
    #path('login/',
    #     LoginView.as_view
    #     (
    #         template_name='app/login.html',
    #         authentication_form=forms.BootstrapAuthenticationForm,
    #         extra_context=
    #         {
    #             'title': 'Log in',
    #             'year' : datetime.now().year,
    #         }
    #     ),
    #     name='login'),
    #path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('',include('blog.urls')),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
]
