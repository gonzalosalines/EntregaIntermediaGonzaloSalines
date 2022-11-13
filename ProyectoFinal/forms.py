from django import forms

class JugadorFormulario(forms.Form):
    
    nombre = forms.CharField(min_length=3,max_length=50)
    apellido = forms.CharField(min_length=3,max_length=50)
    edad= forms.IntegerField()
    puesto= forms.CharField(max_length=30)