from django.urls import path
from .views import  Genero,Pelicula,Cliente, inicio, clienteFormulario, clienteFormulario2,generoFormulario2, peliculaFormulario2, Cliente_View, Genero_View, Pelicula_View,buscar_pelicula
from App_Arriendo_Peliculas import views

from django.contrib import admin


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('index/', views.inicio, name='index'),
    path('Genero/', views.Genero, name='Genero'),
    path('Pelicula/', views.Pelicula, name='Pelicula'),
    path('Cliente/', views.Cliente, name='Cliente'),
    
    path('clienteFormulario2/', views.clienteFormulario2, name='clienteFormulario2'),
    path('clienteFormulario/', views.clienteFormulario, name='clienteFormulario'),
    path('Cliente_View/', Cliente_View, name='Cliente_View'),

    path('generoFormulario2/', views.generoFormulario2, name='generoFormulario2'),
    path('generoFormulario/', views.generoFormulario, name='generoFormulario'),
    path('Genero_View/', Genero_View, name='Genero_View'),

    path('peliculaFormulario2/', views.peliculaFormulario2, name='peliculaFormulario2'),
    path('peliculaFormulario/', views.peliculaFormulario, name='peliculaFormulario'),
    path('Pelicula_View/', Pelicula_View, name='Pelicula_View'),    
    path('buscar_pelicula/', views.buscar_pelicula, name='buscar_pelicula'),

]