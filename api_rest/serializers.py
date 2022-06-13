from rest_framework import serializers
from Juegos.models import Videojuego

class VideojuegoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Videojuego
        fields = ['IdJuego','nombreVideojuego','AñoLanzamiento']

class VideojuegoSerializers2(serializers.ModelSerializer):
    class Meta:
        model = Videojuego
        fields = ['IdJuego','nombreVideojuego','AñoLanzamiento','imagen','categoria']