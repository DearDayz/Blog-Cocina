import json
from . import modeloIA

from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        response_stream = modeloIA.stream_response(message)

        self.send(text_data=json.dumps({"message": message}))

        full_response = ""
        for chunk in response_stream:
            if chunk.choices and chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                full_response += content  # Acumular el contenido
                self.send(text_data=json.dumps({"message": full_response}))
                print(content, end="", flush=True)  # Imprimir el chunk en tiempo real