from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from Juegos.models import Videojuego
from .serializers import VideojuegoSerializers
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
