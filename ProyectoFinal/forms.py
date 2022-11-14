from django import forms

class JugadorFormulario(forms.Form):
    
    nombre = forms.CharField(min_length=3,max_length=50)
    apellido = forms.CharField(min_length=3,max_length=50)
    edad= forms.IntegerField()
    puesto= forms.CharField(max_length=30)

class EquipoFormulario(forms.Form):
    
    club=forms.CharField(max_length=50)
    ciudad = forms.CharField(max_length=45)

class EntrenadorFormulario(forms.Form):
    nombre= forms.CharField(max_length=35)
    apellido= forms.CharField(max_length=35)
    email= forms.EmailField()