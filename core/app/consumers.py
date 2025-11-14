from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
class TestClass(WebsocketConsumer):
    def connect(self):
        self.room_name = "test_room"
        self.room_group_name = "test_group"
        
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        
        print(f"✅ Client is trying to connect...{self.channel_name}")
        self.accept()
        self.send(text_data=json.dumps({"message": "websocket is connected ,Hello Client"}))
        print("🔗 WebSocket connection established")

    def disconnect(self, close_code):
        self.send(text_data=json.dumps({"message": "websocket is disconnected ,Goodbye Client"}))
        print("❌ WebSocket connection closed with code:", close_code)
        self.close()
       
    def receive(self, text_data):
        text_data = json.loads(text_data)
        self.send(text_data=json.dumps({"message": "websocket message received", "data": text_data}))   
    def send_notification(self,event):
        print(event)
        # event = json.loads(event['data'])
        print(event)
        self.send(text_data=json.dumps({"message": "websocket notification received", "notification": event["message"]}))