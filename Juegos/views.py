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