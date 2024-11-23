from django.shortcuts import render
from .context import cargar_contexto_json_cliente, contexto_json_a_string
import requests

# Create your views here.

def chatbot(request):
    # response = requests.get("http://127.0.0.1:8000/blog-api/recetas/")
    # print(response.json())
    # tabla = {"recetas": response.json()}
    # cargar_contexto_json_cliente(tabla)
    # contexto_json_a_string()
    return render(request, "chat/chatbot_original.html")