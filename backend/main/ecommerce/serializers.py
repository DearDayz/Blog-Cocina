from rest_framework import serializers
from .models import Producto, Factura, ProductoFacturado
from login3.serializers import MyUserSerializer
from login3.models import  MyUser



#Serializador de modelo
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'unidad', 'cantidad_disponible', 'precio', 'unidades_vendidas']

class ProductoFacturadoSerializer(serializers.ModelSerializer):
    producto = serializers.SlugRelatedField(
    queryset=Producto.objects.all(),
    slug_field='id'
    )
    class Meta:
        model = ProductoFacturado
        fields = ['id', 'factura', 'producto', 'cantidad']
    
    def to_representation(self, instance):
        # Usar la representación detallada solo al obtener una producto facturado
        representation = super().to_representation(instance)
        # Reemplazar el campo `producto` con el serializador completo del producto
        representation['producto'] = ProductoSerializer(instance.producto).data
        return representation

class FacturaSerializer(serializers.ModelSerializer):
    productos_facturados = ProductoFacturadoSerializer(many=True, read_only=True)
    user = serializers.SlugRelatedField(
    queryset=MyUser.objects.all(),
    slug_field='cedula'
    )
    class Meta:
        model = Factura
        fields = ['id', 'codigo', 'fecha', 'hora', 'user', 'productos_facturados', 'total']

    def to_representation(self, instance):
        # Usar la representación detallada solo al obtener una factura
        representation = super().to_representation(instance)
        
        # Reemplazar el campo `user` con el serializador completo del usuario
        representation['user'] = MyUserSerializer(instance.user).data
        # Eliminar los campos `password` y `tipo` si estásn presentes en la respuesta
        representation['user'].pop('password', None)
        representation['user'].pop('tipo', None)
        
        return representation