from django.urls import path
from django.contrib import admin
from .views import home, index, force_setup

urlpatterns = [
    path('', home, name='home'),
    path('index', index, name='index'),
    path('force_setup', force_setup, name='force_setup'),
]