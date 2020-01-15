from django.urls import re_path, path
from . import views
from .views import *


urlpatterns = [
    path('', views.homepage_view, name='home'),
    path('lokale/<str:slug>/<id>/', views.place_list_view, name='place_list'),
    path('informacje/', views.place_about_view, name='place_about'),
    path('dodaj/', views.place_create_view, name='place_create'),
    path('dodaj/menu/<id>/update/', views.menu_create_view, name='menu_create'),
    
]