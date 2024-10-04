from django.db import models
from ecommerce.models import Ingrediente
from ecommerce.serializers import IngredienteSerializer
from .validadores.validador_receta import validar_solo_letras_con_espacio, validate_no_html, validate_between_zero_and_five,validate_cantidades
from django.core.validators import MaxLengthValidator
# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError


class Receta(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, verbose_name="nombre", validators=[validar_solo_letras_con_espacio, validate_no_html])
    descripcion = models.TextField(verbose_name="descripcion", validators=[MaxLengthValidator(2000), validate_no_html])
    preparacion = models.TextField(verbose_name="preparacion", validators=[MaxLengthValidator(5000), validate_no_html])
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True, verbose_name="Imagen")
    puntuacion = models.FloatField(verbose_name="puntuacion", validators=[validate_between_zero_and_five])
    ingredientes = models.ManyToManyField(Ingrediente, verbose_name="ingredientes")
    cantidades = models.JSONField(verbose_name="cantidades", default=list, validators=[validate_cantidades])


    def __str__(self):
        return self.nombre
    

    def add_ingredients(self, ingredientes_nombres):
        """Método para asociar ingredientes a la receta."""
        for nombre in ingredientes_nombres:
            ingrediente = Ingrediente.objects.get(nombre=nombre)
            self.ingredientes.add(ingrediente)

    @classmethod
    def create_with_ingredients(cls, validated_data):
        """Método de clase para crear una receta con ingredientes."""
        ingredientes_nombres = validated_data.pop('ingredientes')
        receta = cls.objects.create(**validated_data)
         # Realizar validaciones después de que la receta ha sido creada
        print(receta.cantidades)
        print(ingredientes_nombres)

        if len(receta.cantidades) != len(ingredientes_nombres):
            raise ValidationError('La longitud de "cantidades" debe coincidir con la cantidad de ingredientes.')
        receta.add_ingredients(ingredientes_nombres)
        return receta

    def to_representation(self):
        """Método para representar la receta, incluyendo los ingredientes completos."""
        representation = {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "preparacion": self.preparacion,
            "imagen": self.imagen.url if self.imagen else None,
            "puntuacion": self.puntuacion,
            "cantidades": self.cantidades,
            "ingredientes": [
            {
                "id": ingrediente.id,
                "nombre": ingrediente.nombre,
                "unidad": ingrediente.unidad,
                "precio": ingrediente.precio,
                "cantidad_disponible": ingrediente.cantidad_disponible
                    # O cualquier otro atributo que necesites
            }
            for ingrediente in self.ingredientes.all()
        ]
        }
        return representation

    def delete(self, using=None, keep_parents=False):
        if self.imagen and self.imagen.name:
            self.imagen.storage.delete(self.imagen.name)  # Solo eliminar la imagen si existe
        super().delete(using=using, keep_parents=keep_parents)  # Siempre llama al método de eliminación del padre
