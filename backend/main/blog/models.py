from django.utils import timezone
from django.db import models
from ecommerce.models import Producto
from .validadores.validador_receta import validar_solo_letras_con_espacio, validate_no_html, validate_between_zero_and_five,validate_cantidades
from django.core.validators import MaxLengthValidator

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Receta(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, verbose_name="nombre", validators=[validar_solo_letras_con_espacio, validate_no_html])
    descripcion = models.TextField(verbose_name="descripcion", validators=[MaxLengthValidator(2000), validate_no_html])
    preparacion = models.TextField(verbose_name="preparacion", validators=[MaxLengthValidator(5000), validate_no_html])
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True, verbose_name="Imagen")
    puntuacion = models.FloatField(verbose_name="puntuacion", validators=[validate_between_zero_and_five])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre

    def delete(self, using=None, keep_parents=False):
        if self.imagen and self.imagen.name:
            self.imagen.storage.delete(self.imagen.name)  # Solo eliminar la imagen si existe
        super().delete(using=using, keep_parents=keep_parents)  # Siempre llama al método de eliminación del padre

class Ingrediente(models.Model):
    id = models.AutoField(primary_key=True)
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, null=False, blank=False, related_name='ingredientes')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=False, blank=False, related_name='ingredientes')
    unidad = models.CharField(max_length=50, verbose_name="unidad")
    cantidad = cantidad = models.FloatField(verbose_name="cantidad")

    def __str__(self):
        return f"{self.cantidad} {self.unidad} de {self.producto.nombre} para {self.receta.nombre}"





