from django.contrib import admin
from django.urls import path
from .views import createBuilding

urlpatterns = [
    # path('', views.Index.as_view(Index), name="home"),
    path('createBuilding/', createBuilding, name='createBuilding'),
]
