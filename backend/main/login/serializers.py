from rest_framework import serializers
from .models import Trabajador, Usuario

#Serializador de modelo

class TrabajadorSerializer(serializers.ModelSerializer):
     class Meta:
          model = Trabajador
          fields = "__all__"

class UsuarioSerializer(serializers.ModelSerializer):
     class Meta:
          model = Usuario
          fields = "__all__"