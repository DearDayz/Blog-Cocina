from rest_framework import serializers
from .models import Receta, Ingrediente
from ecommerce.models import Producto
from ecommerce.serializers import ProductoSerializer



class IngredienteSerializer(serializers.ModelSerializer):
    producto = serializers.SlugRelatedField(
    queryset=Producto.objects.all(),
    slug_field='id'
    )
    class Meta:
        model = Ingrediente
        fields = ['id', 'receta', 'producto', 'cantidad', 'unidad']
    
    def to_representation(self, instance):
        # Usar la representación detallada solo al obtener una producto facturado
        representation = super().to_representation(instance)
        # Reemplazar el campo `producto` con el serializador completo del producto
        representation['producto'] = ProductoSerializer(instance.producto).data
        return representation


# Serializer para Receta
class RecetaSerializer(serializers.ModelSerializer):
    ingredientes = IngredienteSerializer(many=True, read_only=True)
    class Meta:
        model = Receta
        fields = ["id", 'nombre', 'descripcion', 'preparacion', 'imagen', 'puntuacion', 'ingredientes']
