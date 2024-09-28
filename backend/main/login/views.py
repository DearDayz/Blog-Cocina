from django.shortcuts import render
from rest_framework import generics
from .models import Usuario
from .models import Trabajador
from .serializers import UsuarioSerializer
from .serializers import TrabajadorSerializer
from rest_framework import viewsets

# Create your views here.

#ViewSets

#Usuarios
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Endpoint que busca por cedula usando lookup_field
class UsuarioAPIRetrieveIDCard(generics.RetrieveAPIView):
    lookup_field = 'cedula'  # Cambia el campo de búsqueda a 'cedula'
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


#Trabajador
class TrabajadorViewSet(viewsets.ModelViewSet):
    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer

# Endpoint que busca por cedula usando lookup_field
class TrabajadorAPIRetrieveIDCard(generics.RetrieveAPIView):
    lookup_field = 'cedula'  # Cambia el campo de búsqueda a 'cedula'
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer