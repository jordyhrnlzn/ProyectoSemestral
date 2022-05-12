from django.contrib import admin
from django.urls import path
from. views import index,catalogo

urlpatterns = [
    path('',index,name='index'),
    path('catalogo/',catalogo,name='catalogo'),
]
