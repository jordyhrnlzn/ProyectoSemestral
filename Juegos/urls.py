from django.contrib import admin
from django.urls import path
from. views import index,catalogo,crearcuenta,inciarsesion,inciarsesionADMIN,editarperfil,index2,catalogo2

urlpatterns = [
    path('',index,name='index'),
    path('catalogo/',catalogo,name='catalogo'),
    path('crearcuenta/',crearcuenta,name='crearcuenta'),
    path('inciarsesion/',inciarsesion,name='inciarsesion'),
    path('inciarsesionADMIN/',inciarsesionADMIN,name='inciarsesionADMIN'),
    path('editarperfil/',editarperfil,name='editarperfil'),
    path('index2/',index2,name='index2'),
    path('catalogo2/',catalogo2,name='catalogo2'),
]
