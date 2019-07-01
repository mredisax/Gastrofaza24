from django.urls import re_path, path
from . import views
from .views import (
    homepage_view,
    place_list_view,
    place_create_view,
    menu_create_view,
    place_about_view,
    handler404,
    handler500
    )


urlpatterns = [
    re_path(r'^$', views.homepage_view, name='home'),
    path('lokal/<str:slug>/<id>/', views.place_list_view, name='place_view'),
    path('informacje/', views.place_about_view, name='place_about'),
    path('dodaj/', views.place_create_view, name='place_create'),
    path('dodaj/menu/<id>/update/', views.menu_create_view, name='menu_create'),
    
]
handler404 = views.handler404
handler500 = views.handler500 