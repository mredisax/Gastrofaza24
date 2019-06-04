from django.urls import re_path, path
from . import views
from .views import (
    homepage_view,
    place_list_view,
    place_create_view,
    menu_create_view
    )


urlpatterns = [
    re_path(r'^$', views.homepage_view, name='home'),
    path('lokal/<str:slug>/<id>/', views.place_list_view, name='place_view'),
    path('dodaj/', views.place_create_view, name='place_create'),
    path('dodaj/menu/<id>/update/', views.menu_create_view, name='menu_create'),
    
]