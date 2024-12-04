import json
from . import modeloIA

from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    # def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json["message"]
    #     response_stream = modeloIA.stream_response(message)

    #     self.send(text_data=json.dumps({"type": "user", "message": message}))

    #     self.send(text_data=json.dumps({"type": "chatbot", "message": "Starting"}))

    #     for chunk in response_stream:
    #         if chunk.choices and chunk.choices[0].delta.content:
    #             content = chunk.choices[0].delta.content
    #             self.send(text_data=json.dumps({"type": "chatbot", "message": content}))
    #             print(content, end="", flush=True)
        
    #     self.send(text_data=json.dumps({"type": "chatbot", "message": "Finished"}))

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        response = modeloIA.stream_response(message)

        self.send(text_data=json.dumps({"type": "user", "message": message}))

        self.send(text_data=json.dumps({"type": "chatbot", "message": "Starting"}))

        self.send(text_data=json.dumps({"type": "chatbot", "message": response.text}))
        
        self.send(text_data=json.dumps({"type": "chatbot", "message": "Finished"}))