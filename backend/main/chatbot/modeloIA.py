from openai import OpenAI
from .context import contexto_json_a_string

client = OpenAI(base_url="http://192.168.1.107:1234/v1", api_key="not-needed")

def stream_response(pregunta):
    contexto = contexto_json_a_string()
    response = client.chat.completions.create(
        model="local-model",
        stream=True,
        messages=[
            {
                "role": "system",
                "content": contexto 
            },
            {
                "role": "user",
                "content": pregunta
            }
        ],
        temperature=0.7,
    )
    
    return response