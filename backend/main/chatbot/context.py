import json
import os

def cargar_contexto_json_cliente(tablas):
    # tablas sería un diccionario de diccionarios con la info de cada tabla

    recetas = tablas["recetas"]
    context_json = {
        "instrucciones": "",
        "recetas": {
            "nombres": [],
            "descripciones": [],
            "preparaciones": [],
            "disponibilidad": []
        }
    }
    disponibilidad = context_json["recetas"]["disponibilidad"]
    recetas_json = context_json["recetas"]

    for receta in recetas:
        # listas_ingredientes tiene la lista de ingredientes de todas las recetas

        disponibilidad.append("Disponible")
        i = 0
        for ingrediente in receta["ingredientes"]:
            # receta_ingredientes tiene los ingredientes de una receta
            # Para cada ingrediente se verifica si hay disponibilidad en base a la cantidad necesaria para la receta  
            
            cantidad_ingrediente = receta["cantidades"][i]

            if ingrediente["cantidad_disponible"] < cantidad_ingrediente:
                disponibilidad.pop()
                disponibilidad.append("No disponible")
                break
            i += 1
        
        recetas_json["nombres"].append(receta["nombre"])
        if disponibilidad[-1] == "No disponible":
            recetas_json["descripciones"].append("")
            recetas_json["preparaciones"].append("")
        elif disponibilidad[-1] == "Disponible":
            recetas_json["descripciones"].append(receta["descripcion"])
            recetas_json["preparaciones"].append(receta["preparacion"])
            
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
            contexto["recetas"]["preparaciones"][i] + " " +
            contexto["recetas"]["disponibilidad"][i] + " "
        )
    
    return contexto_formateado

