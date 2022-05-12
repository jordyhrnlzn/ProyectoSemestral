from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'Juegos/index.html')

def catalogo(request):
    return render(request,'Juegos/catalogo.html')