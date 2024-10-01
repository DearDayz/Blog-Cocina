from rest_framework import serializers
from .models import Ingrediente
from .models import Factura
from rest_framework.exceptions import ValidationError as DRFValidationError
from django.core.exceptions import ValidationError

#Serializador de modelo
class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'


class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ['id', 'codigo',"nombreCliente", "formaPago" ,'cedula', 'total', 'ingredientes', 'fecha', 'hora', "cantidades"]  # Campos para lectura
    def to_representation(self, instance):
        # Utiliza el método de representación del modelo
        return instance.to_representation()

class FacturaCreateSerializer(serializers.ModelSerializer):
    ingredientes = IngredienteSerializer(many=True, read_only=True)
    # Campo para aceptar una lista de nombres de ingredientes al crear recetas
    ingredientes = serializers.ListField(
        child=serializers.CharField(),
        write_only=True
    )

    class Meta:
        model = Factura
        fields = ["nombreCliente", "formaPago", 'cedula',"total" ,'ingredientes', "cantidades"]  # Solo los campos necesarios para crear

    def create(self, validated_data):
        # Intenta crear la receta y maneja la validación de la longitud de cantidades
        try:
            return Factura.create_with_ingredients(validated_data)
        except ValidationError as e:
            raise DRFValidationError({'statusText': str(e)})