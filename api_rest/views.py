from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from Juegos.models import Videojuego
from .serializers import VideojuegoSerializers
# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
def listado_videojuegos(request):
    if request.method == 'GET':
        videojuegos = Videojuego.objects.all()
        serializer = VideojuegoSerializers(videojuegos,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VideojuegoSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def addVideojuego(request):
    data = JSONParser().parse(request)
    serializer = VideojuegoSerializers(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def modEliminarVideojuego(request, codigo):
    try:
        v = Videojuego.objects.get(IdJuego = codigo)
    except Videojuego.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VideojuegoSerializers2(v)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 == JSONParser().parse(request)
        serializer = VideojuegoSerializers2(v, data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status == status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        v.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    
def login_app(request):
    us = request.POST['username']
    cl = request.POST['pass']
    try:
        x = Usuario.objects.get(nombreUsuario = us, clave = cl)
        rol2 = Rol.objects.get(nombreRol = 'Administrador')

        if x.rol == rol2:
            contexto ={"usuario": x}
            return render(request, 'x/admin.html',contexto)
        else:
            contexto ={"usuario": x}
            return render(request, 'x/user.html',contexto)
    except Usuario.DoesNotExist:
        messages.error(request, 'Usuario y(o clave incorrecta')
        return redirect('login')
