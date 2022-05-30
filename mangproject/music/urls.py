from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
  path('upload/', views.upload, name="upload"),
  path('<int:playlist_id>/', views.playlist_detail, name="playlist_detail"),
  path('<int:playlist_id>/delete', views.playlist_delete, name="playlist_delete"),
  path('<int:playlist_id>/edit', views.playlist_edit, name="playlist_edit")
]
