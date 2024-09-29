from django.core.exceptions import ValidationError
import re

# Validador de unidad
def unidad(value):
    if not re.match("^[a-zA-Z]+$", value):
        raise ValidationError('La unidad solo debe contener letras.')
    
def validar_solo_letras(valor):
    # Expresión regular que permite letras con acentos, paréntesis, y espacios
    if not re.match(r'^[\(\)a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', valor):
        raise ValidationError(
            'Este campo solo puede contener letras, acentos, paréntesis y espacios.'
        )