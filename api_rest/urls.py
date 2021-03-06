from django.urls import path
from api_rest.views import listado_videojuegos, addVideojuego, modEliminarVideojuego, listado_usuarios, addUsuarios, modEliminarUsuarios, listado_categoria, addCategoria, modEliminarCategoria
from api_rest.viewsLogin import ini_user

urlpatterns = [
    path('listado_videojuegos/',listado_videojuegos,name='listado_videojuegos'),
    path('addVideojuego/',addVideojuego,name='addVideojuego'),
    path('modEliminarVideojuego/<codigo>',modEliminarVideojuego,name='modEliminarVideojuego'),
    path('ini_user/',ini_user,name="ini_user"),
    path('listado_usuarios/',listado_usuarios,name='listado_usuarios'),
    path('addUsuarios/',addUsuarios,name='addUsuarios'), 
    path('modEliminarUsuarios/<codigo>',modEliminarUsuarios,name='modEliminarUsuarios'),
    path('listado_categoria/',listado_categoria,name='listado_categoria'),
    path('addCategoria/',addCategoria,name='addCategoria'), 
    path('modEliminarCategoria/<codigo>',modEliminarCategoria,name='modEliminarCategoria'), 
]