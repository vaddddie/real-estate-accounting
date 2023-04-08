from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.filterBuilding),
    path('createBuilding/', views.createBuilding, name='createBuilding'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
