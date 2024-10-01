from django.core.exceptions import ValidationError
import re
def validar_solo_letras_con_espacio(valor):
    # Expresión regular que permite letras con acentos, paréntesis, y espacios
    if not re.match(r'^[\(\)a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', valor):
        raise ValidationError(
            'Este campo solo puede contener letras, acentos, paréntesis y espacios.'
        )

def validate_no_html(value):
    if re.search(r'<[^>]+>', value):  # Verifica si hay etiquetas HTML
        raise ValidationError('No se permiten etiquetas HTML en este campo.')
    
def validate_between_zero_and_five(value):
    if value < 0 or value > 5:
        raise ValidationError(f'El valor {value} no está entre 0 y 5.')
    
from django.core.exceptions import ValidationError

def validate_cantidades(value):
    if not isinstance(value, list):
        raise ValidationError('El campo "cantidades" debe ser una lista.')
    
    for cantidad in value:
        if not isinstance(cantidad, (float, int)):  # Verifica que cada cantidad sea un float o int
            raise ValidationError('Cada cantidad en "cantidades" debe ser un número (float o int).')