from django.shortcuts import render

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