from django.db import models
from .validadores import validador_ingrediente, validador_factura
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

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
    codigo = models.CharField(max_length=255, unique=True, blank=True)  # Este campo ahora se generará automáticamente
    nombreCliente = models.CharField(max_length=255, validators=[validador_factura.validar_solo_letras_con_espacio])
    formaPago = models.CharField(max_length=255, validators=[validador_factura.validar_solo_letras_con_espacio])
    cedula = models.IntegerField(validators=[validador_factura.cedula_longitud])
    ingredientes = models.ManyToManyField(Ingrediente, verbose_name="ingredientes")
    total = models.FloatField(validators=[MinValueValidator(0.0)])
    cantidades = models.JSONField(verbose_name="cantidades", validators=[validador_factura.validate_cantidades])
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

    def add_ingredients(self, ingredientes_nombres):
        """Método para asociar ingredientes a la factura."""
        for nombre in ingredientes_nombres:
            ingrediente = Ingrediente.objects.get(nombre=nombre)
            self.ingredientes.add(ingrediente)

    @classmethod
    def create_with_ingredients(cls, validated_data):
        """Método de clase para crear una factura con ingredientes."""
        ingredientes_nombres = validated_data.pop('ingredientes')
        factura = cls.objects.create(**validated_data)
         # Realizar validaciones después de que la factura ha sido creada
        if len(factura.cantidades) != len(ingredientes_nombres):
            raise ValidationError('La longitud de "cantidades" debe coincidir con la cantidad de ingredientes.')
        factura.add_ingredients(ingredientes_nombres)
        return factura

    def to_representation(self):
        """Método para representar la factura, incluyendo los ingredientes completos."""
        representation = {
            "id": self.id,
            "codigo": self.codigo,
            "nombreCliente": self.nombreCliente,
            "formaPago": self.formaPago,
            "cedula": self.cedula,
            "ingredientes": [
            {
                "id": ingrediente.id,
                "nombre": ingrediente.nombre,
                "unidad": ingrediente.unidad,
                "precio": ingrediente.precio,
            }
            for ingrediente in self.ingredientes.all()
        ],
            "total": self.total,
            "cantidades": self.cantidades,
            "fecha": self.fecha,
            "hora": self.hora
        }
        return representation
