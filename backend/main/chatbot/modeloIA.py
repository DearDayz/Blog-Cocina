from openai import OpenAI
from .context import contexto_json_a_string
import google.generativeai as genai

api_key = "AIzaSyBmIai1hhtF1r2dg6fMlAYDd3NmjeYFZ9g" 
genai.configure(api_key=api_key)

# client = OpenAI(base_url="http://localhost:1234/v1/", api_key="not-needed")

# def stream_response(pregunta):
#     contexto = contexto_json_a_string()
#     response = client.chat.completions.create(
#         model="local-model",
#         stream=True,
#         messages=[
#             {
#                 "role": "system",
#                 "content": contexto 
#             },
#             {
#                 "role": "user",
#                 "content": pregunta
#             }
#         ],
#         temperature=0.25,
#     )
    
#     return response

def stream_response(user_message):
    model = genai.GenerativeModel("gemini-pro")

    # Inicia una nueva sesión de chat
    chat_session = model.start_chat()

    contexto = contexto_json_a_string()
    chat_session.send_message(contexto)
    
    # Envía un nuevo mensaje y recibe la respuesta en streaming
    response = chat_session.send_message(user_message)
    
    return response