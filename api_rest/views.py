from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from Juegos.models import Videojuego
from Juegos.models import Usuarios
from Juegos.models import Categoria
from .serializers import VideojuegoSerializers
from .serializers import VideojuegoSerializers2
from .serializers import UsuariosSerializers
from .serializers import UsuariosSerializers2
from .serializers import CategoriaSerializers
from .serializers import CategoriaSerializers2
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
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
@permission_classes((IsAuthenticated,))
def addVideojuego(request):
    data = JSONParser().parse(request)
    serializer = VideojuegoSerializers(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
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

@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def listado_usuarios(request):
    if request.method == 'GET':
        usuarios = Usuarios.objects.all()
        serializer = UsuariosSerializers(usuarios,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsuariosSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def addUsuarios(request):
    data = JSONParser().parse(request)
    serializer = UsuariosSerializers(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def modEliminarUsuarios(request, codigo):
    try:
        usuarios = Usuarios.objects.get(IdUsuarios = codigo)
    except Usuarios.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsuariosSerializers2(usuarios)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 == JSONParser().parse(request)
        serializer = UsuariosSerializers2(usuarios, data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status == status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        usuarios.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def listado_categoria(request):
    if request.method == 'GET':
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializers(categoria,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def addCategoria(request):
    data = JSONParser().parse(request)
    serializer = CategoriaSerializers(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def modEliminarCategoria(request, codigo):
    try:
        categoria = Categoria.objects.get(IdCategoria = codigo)
    except Categoria.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategoriaSerializers2(categoria)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 == JSONParser().parse(request)
        serializer = CategoriaSerializers2(categoria, data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status == status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        categoria.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
