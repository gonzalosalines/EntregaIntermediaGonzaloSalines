from django.http import HttpResponse
from ProyectoFinal.models import Curso, Profesor, Estudiante
#from ProyectoFinal.forms import ProfesorFormulario, EstudianteFormulario
from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, "ProyectoFinal/base.html")

def jugadores(request):

    return render(request, "ProyectoFinal/jugadores.html")