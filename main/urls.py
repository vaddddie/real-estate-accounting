from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.test)
    # path('', views.Index.as_view(Index), name="home"),
]
