from django.db import models

# Create your models here.
class Videojuego(models.Model):
    IdJuego = models.AutoField(primary_key=True, verbose_name='ID autoincrementable del juego')
    nombreVideojuego = models.CharField(max_length=20, verbose_name='Nombre del videojuego', blank=False, null=False)
    AñoLanzamiento = models.IntegerField(verbose_name='Año de salida del videojuego')
    imagen = models.ImageField(upload_to='videojuegos')

    def __str__(self):
        return self.nombreVideojuego