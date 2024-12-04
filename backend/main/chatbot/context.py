import json
import os
from ecommerce.models import Producto
from blog.models import Ingrediente

def cargar_contexto_json_cliente(recetas):
    # tablas sería un diccionario de diccionarios con la info de cada tabla
    context_json = {
        "instrucciones": "",
        "recetas": {
            "nombres": [],
            "descripciones": [],
            "preparaciones": [],
            "ingredientes": [],
        }
    }
    recetas_json = context_json["recetas"]

    for receta in recetas:
        ingredientes_str = ""

        for ingrediente in receta["ingredientes"]:
            # Para cada ingrediente se verifica si hay disponibilidad en base a la cantidad necesaria para la receta
            producto = ingrediente["producto"]
            ingredientes_str += f'{ingrediente["cantidad"]}{ingrediente["unidad"]} de {producto["nombre"]}. '
        
        recetas_json["nombres"].append(receta["nombre"])
        recetas_json["descripciones"].append(receta["descripcion"])
        recetas_json["preparaciones"].append(receta["preparacion"])
        recetas_json["ingredientes"].append(ingredientes_str)
            
    context_json["instrucciones"] = (
        "Instrucciones: "
        "1. Eres un chatbot para resolver dudas sobre una tienda de recetas. "
        "2. Solo debes proporcionar información sobre recetas disponibles. "
        "3. Si se pregunta sobre algo no mencionado, indica que no tienes esa información. "
        "Contexto: "
        "Ejemplos de preguntas: "
        "- ¿Qué ingredientes lleva la arepa con queso? "
        "- ¿Tienen recetas para postres? "
        )
    
    path = os.path.join('media', 'context.json')

    with open(path, 'w') as file:
        json.dump(context_json, file, indent=4)
    
# Función que retorna un string con el contexto de la base de datos
def contexto_json_a_string():
    path = os.path.join('media', 'context.json')
    contexto = {}
    
    with open(path, 'r') as file:
        contexto = json.load(file)
    
    contexto_formateado = contexto["instrucciones"] + "Recetas y sus datos: "
    for i in range(0, len(contexto["recetas"]["nombres"])):
        contexto_formateado += (
            contexto["recetas"]["nombres"][i] + ": " +
            contexto["recetas"]["descripciones"][i] + " " +
            contexto["recetas"]["ingredientes"][i] + " " +
            contexto["recetas"]["preparaciones"][i] + " "
        )
    
    return contexto_formateado

