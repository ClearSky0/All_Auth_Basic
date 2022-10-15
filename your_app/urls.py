"""Defines URL patterns for your_app app"""

from django.urls import path

from . import views

app_name = 'your_app'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    path('<slug:option>', views.index, name='index'),
]
