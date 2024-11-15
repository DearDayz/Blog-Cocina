from django.shortcuts import render, get_object_or_404
from blog.models import Receta, Ingrediente
import json

# Create your views here.
def mostrar_html1(request):
    # usamos la forma corta
    return render(request, 'prueba/avion_asientos.html')

def mostrar_receta(request, receta_nombre):
    receta = Receta.objects.get(nombre=receta_nombre)
    ingredientes = receta.ingredientes.all()  # Esto devuelve un queryset de Ingrediente
    receta_data = {
        'id': receta.id,
        'nombre': receta.nombre,
        'descripcion': receta.descripcion,
        'preparacion': receta.preparacion,
        'imagen': receta.imagen.url if receta.imagen else None,
        'ingredientes': [
            {
                'producto': ingrediente.producto.nombre,
                'cantidad': ingrediente.cantidad,
                'unidad': ingrediente.unidad
            }
            for ingrediente in ingredientes
        ]
    }
    receta_json = json.dumps(receta_data)
    print(receta_json)
    return  render(request, 'prueba/receta-prueba.html', {'receta_json': receta_json})