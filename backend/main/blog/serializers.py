from rest_framework import serializers
from .models import Receta
from ecommerce.serializers import IngredienteSerializer
from rest_framework.exceptions import ValidationError as DRFValidationError
from django.core.exceptions import ValidationError



#Serializador de modelo

# Serializer para Receta
class RecetaSerializer(serializers.ModelSerializer):
    # Usamos IngredienteSerializer para mostrar los objetos de los ingredientes
    ingredientes = IngredienteSerializer(many=True, read_only=True)

    # Campo para aceptar una lista de nombres de ingredientes al crear recetas
    ingredientes = serializers.ListField(
        child=serializers.CharField(),
        write_only=True
    )

    class Meta:
        model = Receta
        fields = ["id", 'nombre', 'descripcion', 'preparacion', 'imagen', 'puntuacion', 'ingredientes', "cantidades"]

    def create(self, validated_data):
        # Intenta crear la receta y maneja la validación de la longitud de cantidades
        try:
            return Receta.create_with_ingredients(validated_data)
        except ValidationError as e:
            raise DRFValidationError({'statusText': str(e)})

    def to_representation(self, instance):
        # Utiliza el método de representación del modelo
        return instance.to_representation()