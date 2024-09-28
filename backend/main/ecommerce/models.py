from django.db import models

# Create your models here.
class Ingrediente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="nombre")
    unidad = models.CharField(max_length=50, verbose_name="unidad")
    cantidad_disponible = models.FloatField(verbose_name="cantidad_disponible")
    precio = models.FloatField(verbose_name="precio")
    unidades_vendidas = models.FloatField(verbose_name="unidades_vendidas")

    def __str__(self):
        return f"{self.nombre} ({self.cantidad_disponible} {self.unidad})"
    

class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=255)
    cedula = models.IntegerField()
    ingredientes = models.JSONField(default=list)  # Campo para almacenar ingredientes en formato JSON
    total = models.FloatField()
    fecha = models.DateField(auto_now_add=True)  # Fecha de la factura, se establece automáticamente al crear la factura
    hora = models.TimeField(auto_now_add=True)  # Hora de la factura, se establece automáticamente al crear la factura

    def __str__(self):
        return f"Factura {self.id} - Total: {self.total} - Fecha: {self.fecha} - Hora: {self.hora}"

