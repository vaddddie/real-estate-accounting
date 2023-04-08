from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.filterBuilding),
    path('/createBuilding/', views.createBuilding, name='createBuilding'),
    path('editBuilding/', views.edit_building, name='editBuilding'),
    path('editBuilding/<int:pk>/', views.BuildingUpdateView.as_view(), name='edit_building')
    
]
