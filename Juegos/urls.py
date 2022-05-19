from django.contrib import admin
from django.urls import path
from. views import index,catalogo,crearcuenta,inciarsesion,inciarsesionADMIN

urlpatterns = [
    path('',index,name='index'),
    path('catalogo/',catalogo,name='catalogo'),
    path('crearcuenta/',crearcuenta,name='crearcuenta'),
    path('inciarsesion/',inciarsesion,name='inciarsesion'),
    path('inciarsesionADMIN/',inciarsesionADMIN,name='inciarsesionADMIN'),
]
