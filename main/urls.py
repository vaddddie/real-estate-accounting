from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.filterBuilding),
    path('createBuilding/', views.createBuilding, name='createBuilding'),
    path('editBuilding/<int:pk>/', views.BuildingUpdateView.as_view(), name='edit_building'),
    path('building/<int:pk>/', views.BuildingDetailView.as_view(), name='building_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
