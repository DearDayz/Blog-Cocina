from rest_framework import serializers
from .models import Ingrediente
from .models import Factura

#Serializador de modelo
class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ['id', 'codigo', 'cedula', 'total', 'ingredientes', 'fecha', 'hora']  # Campos para lectura

class FacturaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ['cedula',"total" ,'ingredientes']  # Solo los campos necesarios para crear