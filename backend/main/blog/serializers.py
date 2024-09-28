from rest_framework import serializers
from .models import Receta

#Serializador de modelo

class RecetaSerializer(serializers.ModelSerializer):
     class Meta:
          model = Receta
          fields = "__all__"
