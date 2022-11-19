from django.db import models

# Create your models here.

class Equipo(models.Model):

    club=models.CharField(max_length=50)
    ciudad = models.CharField(max_length=45)

    def __str__(self):
       return f"club: {self.club} - ciudad: {self.ciudad}"


class Jugador(models.Model):
    nombre= models.CharField(max_length=35)
    apellido= models.CharField(max_length=35)
    edad= models.IntegerField()
    puesto= models.CharField(max_length=30)

#create entrenador
class Entrenador(models.Model):
    nombre= models.CharField(max_length=35)
    apellido= models.CharField(max_length=35)
    email= models.EmailField()
    
