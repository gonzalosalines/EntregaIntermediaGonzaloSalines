from django.urls import path
from ProyectoFinal.views import *
#from ProyectoFinal import views   # redundante


urlpatterns = [
    path("inicio/", inicio, name="coder-inicio"),
    path("jugadores/", jugadores, name="coder-jugadores"),
    path("jugador_formulario/", creacion_jugadores, name="coder-jugadores-crear"),
    path("busqueda_jugador.html/", buscar_jugadores, name="coder-jugadores-buscar"),
    path("equipo_formulario/", creacion_equipo, name="coder-equipo-crear"),
    path("busqueda_equipos.html/", buscar_equipo, name="coder-equipo-buscar"),
    path("entrenador_formulario/", creacion_entrenadores, name="coder-entrenadores-crear"),
]