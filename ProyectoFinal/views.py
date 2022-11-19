from django.http import HttpResponse
from ProyectoFinal.models import Equipo, Jugador, Entrenador
from ProyectoFinal.forms import JugadorFormulario, EquipoFormulario, EntrenadorFormulario
from django.shortcuts import render
from django.template import loader 
#from ProyectoFinal import BASE_DIR
import os
#CBV import
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

def inicio(request):
    return render(request, "ProyectoFinal/index.html")

def lista_jugador(request):
    
    jugadores = Jugador.objects.all()

    tabla = {
        "lista_jugador": jugadores
    }
    return render(request, "ProyectoFinal/jugadores.html", tabla)

    #return render(request, "ProyectoFinal/busqueda_jugador.html", {"listado_jugadores": []})


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
            equipos = Equipo.objects.filter(club__icontains=nombre_equipo)
        return render(request, "ProyectoFinal/busqueda_equipos.html", {"listado_equipos": equipos})

    return render(request, "ProyectoFinal/busqueda_equipos.html", {"listado_equipos": []})    

def creacion_entrenadores(request):

    if request.method == "POST":
        formulario = EntrenadorFormulario(request.POST)
        
        if formulario.is_valid():
            # Accedemos al diccionario que contiene
            # la informacion del formulario
            data = formulario.cleaned_data

            entrenador = Entrenador(nombre=data["nombre"], apellido=data["apellido"], email=data["email"])
            entrenador.save()

    formulario = EntrenadorFormulario()
    return render(request, "ProyectoFinal/entrenador_formulario.html", {"formulario": formulario})

def buscar_entrenadores(request):

    if request.GET:
        nombre_entrenador = request.GET.get("nombre_entrenador", "")
        if nombre_entrenador == "":
            entrenadores = []
        else:
            entrenadores = Entrenador.objects.filter(nombre__icontains=nombre_entrenador)
        return render(request, "ProyectoFinal/busqueda_entrenador.html", {"listado_entrenadores": entrenadores})

    return render(request, "ProyectoFinal/busqueda_entrenador.html", {"listado_entrenadores": []})


class ClubList(ListView):

    model = Equipo
    template_name = "ProyectoFinal/list_teams.html"

class ClubDetail(DetailView):

    model = Equipo
    template_name = "ProyectoFinal/teams.html"

class ClubCreation(CreateView):

    model = Equipo
    success_url = "coder/teams.html"
    fields = ["club", "ciudad"]
    template_name = "ProyectoFinal/team_form.html"