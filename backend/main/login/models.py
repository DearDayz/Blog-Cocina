from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="nombre")
    apellido = models.CharField(max_length=255, verbose_name="apellido")
    contraseña = models.CharField(max_length=255, verbose_name="contraseña")  # Considera usar hashing para almacenar contraseñas
    cedula = models.IntegerField(unique=True, verbose_name="cedula")  # Asegúrate de que la cédula sea única
    direccion = models.TextField(verbose_name="direccion")  # Para permitir texto largo
    correo = models.EmailField(max_length=255, unique=True, verbose_name="correo")  # Asegúrate de que el correo sea único
    telefono = models.BigIntegerField( verbose_name="telefono")  # Cambiado a BigIntegerField para almacenar números grandes
    favoritos = models.JSONField(blank=True, null=True, verbose_name="favoritos")  # Campo para almacenar favoritos en formato JSON

    def __str__(self):
        return f"{self.nombre} {self.apellido} - cedula: {self.cedula}"

class Trabajador(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="nombre")
    apellido = models.CharField(max_length=255, verbose_name="apellido")
    contraseña = models.CharField(max_length=255, verbose_name="contraseña")
    cedula = models.IntegerField(verbose_name="cedula", unique=True)
    direccion = models.TextField(verbose_name="dirección")
    correro = models.EmailField(max_length=255, unique=True ,verbose_name="correo")
    telefono = models.BigIntegerField(verbose_name="telefono")
    cargo = models.CharField(max_length=255, verbose_name="cargo")

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.cargo}"
    
    class Meta:
        verbose_name_plural = "trabajadores"