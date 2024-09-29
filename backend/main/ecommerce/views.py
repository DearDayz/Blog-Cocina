from django.shortcuts import render
from rest_framework import generics
from .models import Factura
from .models import Ingrediente
from .serializers import FacturaSerializer, FacturaCreateSerializer
from .serializers import IngredienteSerializer
from rest_framework import viewsets

# Create your views here.

#ViewSets

#Ingredientes
class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

# Endpoint que busca por nombre usando lookup_field
class IngredienteAPIRetrieveName(generics.RetrieveAPIView):
    lookup_field = 'nombre'  # Cambia el campo de búsqueda a 'nombre'
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

#Facturas
class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    def get_serializer_class(self):
        if self.request.method in ['POST']:
            return FacturaCreateSerializer  # Usa el serializer de creación para POST
        return FacturaSerializer  # Usa el serializer de lectura para GET

