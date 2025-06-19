# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Genero, Pelicula, Cliente, Pelicula
from .forms import ClienteFormulario2, GeneroFormulario2, PeliculaFormulario2

from django.http import HttpResponse

# def lista_estudiantes(request):
#     estudiantes = Estudiante.objects.all()
#     return render(request, 'estudiantes_list.html', {'estudiantes': estudiantes})

# def detalle_estudiante(request, pk):
#     estudiante = get_object_or_404(Estudiante, pk=pk)
#     return render(request, 'estudiante_detail.html', {'estudiante': estudiante})

# def entregables(request):
#     return render(request, "AppCoder/entregables.html")

def inicio(request):
    return render(request, "App_Arriendo_Peliculas/index.html")

def Genero_View(request):
    return render(request, "App_Arriendo_Peliculas/Genero.html")

def Pelicula_View(request):
    return render(request, "App_Arriendo_Peliculas/Pelicula.html")

def Cliente_View(request):
    return render(request, "App_Arriendo_Peliculas/Cliente.html")

def clienteFormulario(request):
   if request.method == "POST":
        cliente =  Cliente(nombre=request.POST['nombre'],email=(request.POST['email']))
        cliente.save()

        return render(request, "App_Arriendo_Peliculas/formulario/clienteFormulario.html", {"mensaje": "Cliente guardado"})
   return render(request, "App_Arriendo_Peliculas/formulario/clienteFormulario.html")


def generoFormulario(request):
   if request.method == "POST":
        genero =  Genero(nombre=request.POST['nombre'])
        genero.save()

        return render(request, "App_Arriendo_Peliculas/formulario/generoFormulario.html", {"mensaje": "Genero guardado"})
   return render(request, "App_Arriendo_Peliculas/formulario/generoFormulario.html")


def peliculaFormulario(request):
   if request.method == "POST":
       pelicula = Pelicula(
                  titulo=request.POST['titulo'],
                  anio=request.POST['anio'],
                  disponible = request.POST.get('disponible') == 'on')
                  #disponible=request.POST['disponible'])
       pelicula.save()
       return render(request, "App_Arriendo_Peliculas/formulario/peliculaFormulario.html", {"mensaje": "Pelicula guardada"})
   return render(request, "App_Arriendo_Peliculas/formulario/peliculaFormulario.html")



def clienteFormulario2(request):
    if request.method == "POST":
        miFormulario = ClienteFormulario2(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cliente =  Cliente(nombre=request.POST['nombre'],email=(request.POST['email']))
            cliente.save()
            return render(request, "App_Arriendo_Peliculas/index.html")
    else:
        miFormulario = ClienteFormulario2()

    return render(request, "App_Arriendo_Peliculas/formulario/clienteFormulario2.html", {"miFormulario": miFormulario})



def generoFormulario2(request):
    if request.method == "POST":
        miFormulario = GeneroFormulario2(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            genero =  Genero(nombre=request.POST['nombre'])
            genero.save()
            return render(request, "App_Arriendo_Peliculas/index.html")
    else:
        miFormulario = GeneroFormulario2()

    return render(request, "App_Arriendo_Peliculas/formulario/generoFormulario2.html", {"miFormulario": miFormulario})


def peliculaFormulario2(request):
    if request.method == "POST":
        miFormulario = PeliculaFormulario2(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            pelicula = Pelicula(
                  titulo=request.POST['titulo'],
                  anio=request.POST['anio'],
                  disponible = request.POST.get('disponible') == 'on')
                  #disponible=request.POST['disponible'])
            pelicula.save()
            return render(request, "App_Arriendo_Peliculas/index.html")
    else:
        miFormulario = PeliculaFormulario2()

    return render(request, "App_Arriendo_Peliculas/formulario/peliculaFormulario2.html", {"miFormulario": miFormulario})


def buscar_pelicula(request):
    resultados = []
    if 'nombre' in request.GET:
        nombre = request.GET['nombre']
        resultados = Pelicula.objects.filter(titulo__icontains=nombre)
    return render(request, "App_Arriendo_Peliculas/resultados_busqueda.html", {"resultados": resultados})