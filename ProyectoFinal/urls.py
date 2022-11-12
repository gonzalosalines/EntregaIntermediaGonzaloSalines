from django.urls import path
from ProyectoFinal.views import *

urlpatterns = [
    path("inicio/", inicio, name="coder-inicio"),
    path("estudiantes/", jugadores, name="coder-jugadores"),
    
]