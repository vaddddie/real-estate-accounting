from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.filterBuilding),
    path('createBuilding/', views.createBuilding, name='createBuilding'),
]
