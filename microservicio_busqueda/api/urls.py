from django.urls import re_path
from api import views

urlpatterns = [
    re_path(r'^searchComics$', views.busquedaApi)
]
