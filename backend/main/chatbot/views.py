from django.shortcuts import render

# Create your views here.

def chatbot(request):
    # response = requests.get("http://127.0.0.1:8000/blog/recetas/")
    # tabla = {"recetas": response.json()}
    # cargar_contexto_json_cliente(tabla)
    return render(request, "chat/chatbot_original.html")