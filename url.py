from django.contrib import admin
from django.urls import path, include
from Hello import views

urlpatterns = [
    path("", views.index, name='Home'),
    path("about", views.about, name='About'),
    path("service", views.service, name='Service')

]