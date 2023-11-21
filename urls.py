# smartscoreApp/urls.py
from django.urls import path
from .views import index, home

urlpatterns = [
    path('index/', index, name='index'),
    path('home/', home, name='home'),
]
