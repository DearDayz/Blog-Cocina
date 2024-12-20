from django.utils import timezone
from django.db import models
from ecommerce.models import Producto
from .validadores.validador_receta import validar_solo_letras_con_espacio, validate_no_html, validate_between_zero_and_five,validate_cantidades
from django.core.validators import MaxLengthValidator
from login3.models import MyUser
from django.db.models.signals import post_save

class Category(models.Model):
    name = models.CharField(max_length=50)
    descripcion = models.TextField(verbose_name="descripcion", validators=[MaxLengthValidator(2000), validate_no_html], blank=True, null=True)
    imagen = models.ImageField(upload_to='categorias/', blank=True, null=True, verbose_name="Imagen")
    
    def __str__(self):
        return self.name

class Receta(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, verbose_name="nombre", validators=[validar_solo_letras_con_espacio, validate_no_html])
    descripcion = models.TextField(verbose_name="descripcion", validators=[MaxLengthValidator(2000), validate_no_html])
    preparacion = models.TextField(verbose_name="preparacion", validators=[MaxLengthValidator(5000), validate_no_html])
    imagen = models.ImageField(upload_to='recetas/', blank=True, null=True, verbose_name="Imagen")
    puntuacion = models.FloatField(verbose_name="puntuacion", validators=[validate_between_zero_and_five], blank=True, default=0)
    category = models.ManyToManyField(Category, related_name='recetas')
    date_modified = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

    def delete(self, using=None, keep_parents=False):
        if self.imagen and self.imagen.name:
            self.imagen.storage.delete(self.imagen.name)  # Solo eliminar la imagen si existe
        super().delete(using=using, keep_parents=keep_parents)  # Siempre llama al método de eliminación del padre

    
    def get_puntuacion(self):
        valoraciones = Valoracion.objects.filter(receta=self)
        if valoraciones.exists():
            self.puntuacion = round(valoraciones.aggregate(models.Avg('puntuacion'))['puntuacion__avg'], 1)
            self.save()

        else:
            self.puntuacion = 0
            self.save()

class Ingrediente(models.Model):
    id = models.AutoField(primary_key=True)
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, null=False, blank=False, related_name='ingredientes')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=False, blank=False, related_name='ingredientes')
    unidad = models.CharField(max_length=50, verbose_name="unidad", blank=True)
    cantidad = cantidad = models.FloatField(verbose_name="cantidad")

    def __str__(self):
        return f"{self.cantidad} {self.unidad} de {self.producto.nombre} para {self.receta.nombre}"

    def save(self, *args, **kwargs):
        self.unidad = self.producto.unidad
        super().save(*args, **kwargs)


class Favoritos(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=False, blank=False, to_field="cedula", related_name='usuario')
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, null=False, blank=False, related_name='receta')

    def __str__(self):
        return f"{self.receta.nombre}"

class Valoracion(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE,  verbose_name="usuario", to_field="cedula")
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, verbose_name="receta")
    puntuacion = models.PositiveIntegerField(verbose_name="puntuacion")

    class Meta:
        verbose_name_plural = "valoraciones"
    
    def __str__(self):
        return f"Valoración de {self.user.username} para {self.receta} de {self.puntuacion} estrellas"

def create_puntuacion(sender, instance, created, **kwargs):
    val = instance
    receta = val.receta
    receta.get_puntuacion()

post_save.connect(create_puntuacion, sender=Valoracion)
