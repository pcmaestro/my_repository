from . import views
from django.urls import path

urlpatterns = [
    path("", views.inicio),
    path("guardar-formulario", views.guardar_formulario)
]