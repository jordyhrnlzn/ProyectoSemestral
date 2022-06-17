from rest_framework import serializers
from Juegos.models import Videojuego, Usuarios, Categoria

class VideojuegoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Videojuego
        fields = ['IdJuego','nombreVideojuego','AñoLanzamiento']

class UsuariosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['IdUsuarios','nombreUsuario']

class UsuariosSerializers2(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['IdUsuarios','nombreUsuario']

class VideojuegoSerializers2(serializers.ModelSerializer):
    class Meta:
        model = Videojuego
        fields = ['IdJuego','nombreVideojuego','AñoLanzamiento','imagen','categoria']


class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['IdCategoria','nombreCategoria']


class CategoriaSerializers2(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['IdCategoria','nombreCategoria']