# Create your models here.
from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    anio = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)
    

    def __str__(self):
        return self.titulo

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # peliculas_alquiladas = models.ManyToManyField(Pelicula, blank=True)

    def __str__(self):
        return self.nombre