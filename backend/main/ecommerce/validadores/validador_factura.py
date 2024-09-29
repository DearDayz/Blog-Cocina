from django.core.exceptions import ValidationError

# Validador de unidad
def cedula_longitud(value):
    if len(str(value))<7 or len(str(value))>8:
        raise ValidationError('Cedula incorrecta')
    