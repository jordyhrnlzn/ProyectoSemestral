from django.shortcuts import render, redirect
from .models import Videojuego, Categoria


# Create your views here.
def index(request):
    return render(request,'Juegos/index.html')

def catalogo(request):
    return render(request,'Juegos/catalogo.html')

def inciarsesion(request):
    return render(request,'Juegos/inciarsesion.html')

def crearcuenta(request):
    return render(request,'Juegos/crearcuenta.html')

def inciarsesionADMIN(request):
    return render(request,'Juegos/inciarsesionADMIN.html')

def editarperfil(request):
    return render(request,'Juegos/editarperfil.html')

def index2(request):
    return render(request,'Juegos/index2.html')

def catalogo2(request):
    return render(request,'Juegos/catalogo2.html')

def listado(request):
    videojuegos = Videojuego.objects.all()
    contexto = {"lista_v": videojuegos}
    return render(request,'Juegos/listadoM.html',contexto)

def formulario(request):
    categorias = Categoria.objects.all()
    contexto = {"lista_c": categorias}
    return render(request,'Juegos/formulario.html',contexto)

def registrar(request):
    nombre2 = request.POST[nombre1]
    año2 = request.POST[año1]
    imagen2 = request.FILES[imagen1]
    categoria2 = request.POST[categoria1]

    categoria3 = Categoria.objects.get(IdCategoria = categoria2)
    Videojuego.objects.create(nombreVideojuego = nombre2, AñoLanzamiento = año2, imagen = imagen2, categoria = categoria2)
    return redirect('formulario')