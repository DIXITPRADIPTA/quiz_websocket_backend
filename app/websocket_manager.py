from fastapi import WebSocket
from typing import Dict


class WebSocketManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, student_id: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[student_id] = websocket

    def disconnect(self, student_id: str):
        self.active_connections.pop(student_id, None)

    async def send_message(self, student_id: str, message: dict):
        websocket = self.active_connections.get(student_id)
        if websocket:
            await websocket.send_json(message)

    async def broadcast(self, message: dict):
        for websocket in self.active_connections.values():
            await websocket.send_json(message)


# Initialize WebSocket Manager
websocket_manager = WebSocketManager()
