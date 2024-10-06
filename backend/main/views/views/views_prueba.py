from django.shortcuts import render, get_object_or_404
from blog.models import Receta
import json

# Create your views here.
def mostrar_html1(request):
    # usamos la forma corta
    return render(request, 'prueba/avion_asientos.html')

def mostrar_receta(request, receta_nombre):
    receta = get_object_or_404(Receta, nombre=receta_nombre)
    print(receta.to_representation())
    print(type(receta.to_representation()))
    receta_json = json.dumps(receta.to_representation())
    print(receta_json)
    return  render(request, 'prueba/receta-prueba.html', {'receta_json': receta_json})