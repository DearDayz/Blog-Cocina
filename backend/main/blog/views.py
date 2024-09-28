from django.shortcuts import render
from rest_framework import generics
from .models import Receta
from .serializers import RecetaSerializer
from rest_framework import viewsets

# Create your views here.
class RecetaAPIList(generics.ListAPIView):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer


#ViewSets
class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer