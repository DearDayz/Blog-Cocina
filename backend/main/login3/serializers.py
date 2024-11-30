from rest_framework import serializers
from .models import MyUser

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
            "is_active",
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'is_active': {'required': False}
        }

    def create(self, validated_data):
        validated_data['is_active'] = True 
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

