from django.db import models

# Create your models here.
class Categoria(models.Model):
    IdCategoria = models.AutoField(primary_key=True, verbose_name='ID autoincrementable de la categori')
    nombreCategoria = models.CharField(max_length=20, verbose_name='Nombre de la categoria', blank=False, null=False)

    def __str__(self):
        return self.nombreVideojuego

class Videojuego(models.Model):
    nombreVideojuego = models.CharField(max_length=20, verbose_name='Nombre del videojuego', blank=False, null=False)
    AñoLanzamiento = models.IntegerField(verbose_name='Año de salida del videojuego')
    imagen = models.ImageField(upload_to='videojuegos')

    def __str__(self):
        return self.nombreVideojuego