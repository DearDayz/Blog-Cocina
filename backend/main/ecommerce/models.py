from django.db import models
from .validadores import validador_ingrediente, validador_factura
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from login3.models import MyUser

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="nombre", unique=True, validators=[validador_ingrediente.validar_solo_letras])
    unidad = models.CharField(max_length=50, verbose_name="unidad", validators=[validador_ingrediente.unidad])
    cantidad_disponible = models.FloatField(verbose_name="cantidad_disponible", validators=[MinValueValidator(0.0)])
    precio = models.DecimalField(verbose_name="precio", validators=[MinValueValidator(0.0)], decimal_places=2, max_digits=6, default=0)
    unidades_vendidas = models.DecimalField(verbose_name="unidades_vendidas",max_digits= 6, validators=[MinValueValidator(0.0)], decimal_places=2, default=0)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True, verbose_name="Imagen")

    def save(self, *args, **kwargs):
        self.unidad = self.unidad.lower()
        super().save(*args, **kwargs)  # Llama al método save() original para guardar la instancia
        
    def __str__(self):
        return f"{self.nombre} ({self.cantidad_disponible} {self.unidad})"
    


class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=255, unique=True, blank=True)  # Este campo ahora se generará automáticamente
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE,  verbose_name="usuario", to_field="cedula")
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


class ProductoFacturado(models.Model):
    id = models.AutoField(primary_key=True)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE,  verbose_name="factura", related_name='productos_facturados')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,  verbose_name="producto_facturado" , related_name='productos_facturados')
    cantidad = models.FloatField(verbose_name="cantidad", validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f"{self.cantidad} de {self.producto.nombre} en factura {self.factura.codigo}"