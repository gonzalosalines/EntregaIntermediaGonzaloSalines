from django.urls import path
from ProyectoFinal.views import *
#from ProyectoFinal import views   # redundante


urlpatterns = [
    path("inicio/", inicio, name="coder-inicio"),
    path("jugadores/", lista_jugador, name="coder-jugadores"),
    path("jugador_formulario/", creacion_jugadores, name="coder-jugadores-crear"),
    path("busqueda_jugador.html/", buscar_jugadores, name="coder-jugadores-buscar"),
    path("equipo_formulario/", creacion_equipo, name="coder-equipo-crear"),
    path("busqueda_equipos.html/", buscar_equipo, name="coder-equipo-buscar"),
    path("entrenador_formulario/", creacion_entrenadores, name="coder-entrenadores-crear"),
    path("busqueda_entrenador.html/", buscar_entrenadores, name="coder-entrenadores-buscar"),

    path("teams/", ClubList.as_view(), name="coder-teams"),
    path("teams/detail/<pk>/", ClubDetail.as_view(), name="coder-team-detail"),
    path("teams/create/", ClubCreation.as_view(), name="coder-team-create"),
    path("teams/update/<pk>/", ClubUpdate.as_view(), name="coder-team-update"),
    path("entregables/delete/<pk>/", ClubDelete.as_view(), name="coder-team-delete"),
    

]