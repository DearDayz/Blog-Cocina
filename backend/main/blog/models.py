from django.db import models

# Create your models here.
from django.db import models

class Receta(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, verbose_name="nombre")
    descripcion = models.TextField(verbose_name="descripcion")
    preparacion = models.TextField(verbose_name="preparacion")
    imagen = models.ImageField(upload_to='imagenes/', blank=False, null=False, verbose_name="imagen")
    puntuacion = models.FloatField(verbose_name="puntuacion")
    ingredientes = models.JSONField(verbose_name="ingredientes", default=list)  # Usamos JSONField para almacenar los ingredientes

    def __str__(self):
        return self.nombre
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
