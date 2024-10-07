from django.core.exceptions import ValidationError
import re
def validar_username(valor):
    if not re.match(r'^[a-zA-Z0-9áéíóúÁÉÍÓÚüÜ_-]+$', valor):
        raise ValidationError(
            'El nombre de usuario solo puede contener letras, acentos, y los simbolos "-" "_".'
        )
    elif len(valor) < 5:
        raise ValidationError(
            'El nombre de usuario debe tener más de 4 caracteres.'
        )

def validar_correo(valor):
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', valor): 
        raise ValidationError('Debe ingresar un correo válido.')
    
def validar_telefono(value):
    if value > 4269999999 or value < 4120000000:
        raise ValidationError('Ingrese un número de teléfono válido')

def validar_direccion(valor):
    if not re.match(r'^[0-9a-zA-Z\s.,#-]+$', valor): 
        raise ValidationError('Debe ingresar una dirección válida.')
    
def validar_cedula(value):
    if value > 40000000 or value < 10000000:
        raise ValidationError('Debe ingresar una cédula válida')

def validar_tipo(value):
    tipos_usuarios = ["Administrador", "Cliente"]
    if not value in tipos_usuarios:
        raise ValidationError('Debe ingresar un tipo de usuario válido')
    
def validar_nombre(valor):
    if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚüÜ\s'ñÑ-]+$", valor): 
        raise ValidationError('Debe ingresar un nombre válido.')
    
def validar_favoritos(valor):
    if not valor is dict: 
        raise ValidationError('Debe agregar las recetas a favoritos en formato JSON')