from django.urls import path
from ProyectoFinal.views import *
from ProyectoFinal import views   #posiblemente redundante


urlpatterns = [
    path("inicio/", inicio, name="coder-inicio"),
    path("jugadores/", jugadores, name="coder-jugadores"),
    
]