from django.http import HttpResponse
from ProyectoFinal.models import Equipo, Jugador, Entrenador
from ProyectoFinal.forms import JugadorFormulario, EquipoFormulario, EntrenadorFormulario
from django.shortcuts import render
from django.template import loader # es realmente necesario?

# Create your views here.

def inicio(request):
    return render(request, "ProyectoFinal/index.html")

def jugadores(request):

    return render(request, "ProyectoFinal/jugadores.html")


def creacion_jugadores(request):

    if request.method == "POST":
        formulario = JugadorFormulario(request.POST)
        
        if formulario.is_valid():
            # Accedemos al diccionario que contiene
            # la informacion del formulario
            data = formulario.cleaned_data

            jugador = Jugador(nombre=data["nombre"], apellido=data["apellido"], edad=data["edad"],puesto=data["puesto"])
            jugador.save()

    formulario = JugadorFormulario()
    return render(request, "ProyectoFinal/jugador_formulario.html", {"formulario": formulario})

def buscar_jugadores(request):
#creacion de buscador
    if request.GET:
        nombre_jugador = request.GET.get("nombre_jugador", "")
        if nombre_jugador == "":
            jugadores = []
        else:
            jugadores = Jugador.objects.filter(nombre__icontains=nombre_jugador)
        return render(request, "ProyectoFinal/busqueda_jugador.html", {"listado_jugadores": jugadores})

    return render(request, "ProyectoFinal/busqueda_jugador.html", {"listado_jugadores": []})

    

def creacion_equipo(request):

    if request.method == "POST":
        formulario = EquipoFormulario(request.POST)
        
        if formulario.is_valid():
            # Accedemos al diccionario que contiene
            # la informacion del formulario
            data = formulario.cleaned_data

            jugador = Equipo(club=data["club"], ciudad=data["ciudad"])
            jugador.save()

    formulario = EquipoFormulario()
    return render(request, "ProyectoFinal/equipo_formulario.html", {"formulario": formulario})

def buscar_equipo(request):
#creacion de buscador
    if request.GET:
        nombre_equipo = request.GET.get("nombre_equipo", "")
        if nombre_equipo == "":
            equipos = []
        else:
            equipos = Equipo.objects.filter(nombre__icontains=nombre_equipo)
        return render(request, "ProyectoFinal/busqueda_equipos.html", {"listado_equipos": equipos})

    return render(request, "ProyectoFinal/busqueda_equipos.html", {"listado_equipos": []})    