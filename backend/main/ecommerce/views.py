from django.shortcuts import render
from rest_framework import generics
from .models import Factura
from .models import Ingrediente
from .serializers import FacturaSerializer, FacturaCreateSerializer
from .serializers import IngredienteSerializer
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample
from .tables import get_table_ingrediente, get_example_ingrediente, post_table_ingrediente, post_example_ingrediente, get_table_factura, get_example_factura, post_table_factura, post_example_factura


# Create your views here.

#ViewSets

#Ingredientes
class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

    @extend_schema(
        responses={
            200: OpenApiResponse(
                description=get_table_ingrediente,
                response=IngredienteSerializer(many=True),  # Documentar usando el serializer asda
                examples=[
                    OpenApiExample(
                        'Ejemplo de Obtencion de un get',
                        value=get_example_ingrediente)]
            ),
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    
    @extend_schema(
        request=IngredienteSerializer,  # Documentar el request usando el serializer
        responses={
            201: OpenApiResponse(
                description=post_table_ingrediente,
                response=IngredienteSerializer(),
                examples=[
                    OpenApiExample(
                        'Ejemplo de cuerpo de solicitud',
                        value=[post_example_ingrediente]
                    )
                ]
            ),
            400: OpenApiResponse(
                description='Error de validación',
            ),
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

# Endpoint que busca por nombre usando lookup_field
class IngredienteAPIRetrieveName(generics.RetrieveAPIView):
    lookup_field = 'nombre'  # Cambia el campo de búsqueda a 'nombre'
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

#Facturas
class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    def get_serializer_class(self):
        if self.request and self.request.method in ['POST']:
            return FacturaCreateSerializer  # Usa el serializer de creación para POST
        return FacturaSerializer  # Usa el serializer de lectura para GET
    
    @extend_schema(
        responses={
            200: OpenApiResponse(
                description=get_table_factura,
                response=FacturaSerializer(many=True),  # Documentar usando el serializer asda
                examples=[
                    OpenApiExample(
                        'Ejemplo de Obtencion de un get',
                        value=get_example_factura)]
            ),
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(
        request=FacturaSerializer,  # Documentar el request usando el serializer
        responses={
            201: OpenApiResponse(
                description=post_table_factura,
                response=FacturaSerializer(),
                examples=[
                    OpenApiExample(
                        'Ejemplo de cuerpo de solicitud',
                        value=[post_example_factura]
                    )
                ]
            ),
            400: OpenApiResponse(
                description='Error de validación',
            ),
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class FacturaAPIRetrieveByCedula(generics.ListAPIView):
    serializer_class = FacturaSerializer

    def get_queryset(self):
        cedula = self.kwargs.get('cedula')
        return Factura.objects.filter(cedula=cedula)