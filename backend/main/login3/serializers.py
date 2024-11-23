from rest_framework import serializers
from .models import MyUser
from blog.models import Favoritos

#Serializador de modelo

class MyUserSerializer(serializers.ModelSerializer):
     class Meta:
          model = MyUser
          fields = [
               "id",
               "username",
               "nombre",
               "apellido",
               "cedula",
               "correo",
               "direccion",
               "telefono",
               "tipo",
               "password",
               ]
          extra_kwargs = {
               'password': {'write_only': True}
          }

     # Función para crear el usuario con el .set_password (que la pasa a un hash)
     def create(self, validated_data):
          password = validated_data.pop('password', None)
          instance = self.Meta.model(**validated_data)
          if password is not None:
               instance.set_password(password)
          instance.save()
          return instance


class FavoritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favoritos
        fields = ['id', 'usuario', 'receta']  