from django.urls import path

from . import views

ulrpatterns = [
    path('', views.index, name="index"),
    path('sobre/', views.sobre, name='sobre')
]