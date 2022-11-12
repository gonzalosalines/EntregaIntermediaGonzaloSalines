from django.http import HttpResponse
from ProyectoFinal.models import Equipo, Jugador, Entrenador
#from ProyectoFinal.forms import ProfesorFormulario, EstudianteFormulario
from django.shortcuts import render
from django.template import loader # es realmente necesario?

# Create your views here.

def inicio(request):
    return render(request, "ProyectoFinal/base.html")

def jugadores(request):

    return render(request, "ProyectoFinal/jugadores.html")