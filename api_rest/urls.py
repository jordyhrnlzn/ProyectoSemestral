from django.urls import path
from api_rest.views import listado_videojuegos, addVideojuego, modEliminarVideojuego

urlpatterns = [
    path('listado_videojuegos/',listado_videojuegos,name='listado_videojuegos'),
    path('addVideojuego/',addVideojuego,name='addVideojuego'),
    path('modEliminarVideojuego/',modEliminarVideojuego,name='modEliminarVideojuego'),
]