from django.core.exceptions import ValidationError
from django.core.exceptions import ValidationError
import re
# Validador de unidad
def cedula_longitud(value):
    if len(str(value))<7 or len(str(value))>8:
        raise ValidationError('Cedula incorrecta')

def validate_cantidades(value):
    if not isinstance(value, list):
        raise ValidationError('El campo "cantidades" debe ser una lista.')
    
    for cantidad in value:
        if not isinstance(cantidad, (float, int)):  # Verifica que cada cantidad sea un float o int
            raise ValidationError('Cada cantidad en "cantidades" debe ser un número (float o int).')

def validar_solo_letras_con_espacio(valor):
    # Expresión regular que permite letras con acentos, paréntesis, y espacios
    if not re.match(r'^[\(\)a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', valor):
        raise ValidationError(
            'Este campo solo puede contener letras, acentos, paréntesis y espacios.'
        )