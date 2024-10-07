from openai import OpenAI

client = OpenAI(base_url="http://192.168.1.107:1234/v1", api_key="not-needed")

def stream_response(pregunta):
    response = client.chat.completions.create(
        model="local-model",
        stream=True,
        messages=[
            {
                "role": "system",
                "content": "You are a chatbot, which will be used to resolve the doubts of the users of a web store that sells ingredients to make recipes and also mostly to recommend to the users recipes that they want based on those that the store has available, for this you will get the information from the file that I am going to pass on to you, remember do not mention recipes that are not mentioned in the file and if they ask you about something that is not in the file, say that the store does not have that information, do not mention anything in the file, and Remember you are a chatbot from a store, not a conventional AI\nContext:\n[CONTEXT 0]:\n<document_metadata>\nsourceDocument: recetas.txt\npublished: 7/9/2024, 15:30:38\n</document_metadata>\n\nEsto es un archivo que proporciona informacion sobre la tienda de recetas \"AlvarezCorps\"\r\n\r\nRecetas disponibles:\r\n1) Arepa con queso: este es un plato tipico venezolano. Consta de los siguientes ingredientes: 250kg de harina de maiz, 0,5 litros de agua, sal al gusto y 500 gramos de queso\n[END CONTEXT 0]\n\n"
            },
            {
                "role": "user",
                "content": pregunta
            }
        ],
        temperature=0.7,
    )
    
    return response