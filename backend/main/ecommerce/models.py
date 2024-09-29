from django.db import models
from .validadores import validador_ingrediente, validador_factura
from django.core.validators import MinValueValidator

# Create your models here.
class Ingrediente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="nombre", unique=True, validators=[validador_ingrediente.validar_solo_letras])
    unidad = models.CharField(max_length=50, verbose_name="unidad", validators=[validador_ingrediente.unidad])
    cantidad_disponible = models.FloatField(verbose_name="cantidad_disponible", validators=[MinValueValidator(0.0)])
    precio = models.FloatField(verbose_name="precio", validators=[MinValueValidator(0.0)])
    unidades_vendidas = models.FloatField(verbose_name="unidades_vendidas", validators=[MinValueValidator(0.0)])

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.lower()
        self.unidad = self.unidad.lower()
        super().save(*args, **kwargs)  # Llama al método save() original para guardar la instancia
        
    def __str__(self):
        return f"{self.nombre} ({self.cantidad_disponible} {self.unidad})"
    

class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=255, unique=True)  # Este campo ahora se generará automáticamente
    cedula = models.IntegerField(validators=[validador_factura.cedula_longitud])
    ingredientes = models.JSONField(default=list)  # Campo para almacenar ingredientes en formato JSON
    total = models.FloatField(validators=[MinValueValidator(0.0)])
    fecha = models.DateField(auto_now_add=True)  # Fecha de la factura, se establece automáticamente al crear la factura
    hora = models.TimeField(auto_now_add=True)  # Hora de la factura, se establece automáticamente al crear la factura

    def save(self, *args, **kwargs):
        if not self.codigo:  # Si el código no existe aún
            last_factura = Factura.objects.order_by('id').last()  # Obtiene la última factura creada, ordenada por 'id'
            if last_factura:
                last_codigo = int(last_factura.codigo)  # Convierte el último código en un número entero
                self.codigo = f'{last_codigo + 1:07d}'  # Genera el nuevo código con formato de 7 dígitos
            else:
                self.codigo = '0000001'  # Si es la primera factura, comienza con '0000001'
        super().save(*args, **kwargs)  # Llama al método save() original para guardar la instancia

    def __str__(self):
        return f"Factura {self.id} - Total: {self.total} - Fecha: {self.fecha} - Hora: {self.hora}"

