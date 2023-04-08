from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.test),
    path('createBuilding/', views.createBuilding, name='createBuilding'),
]
