import json
from fastapi import WebSocket, WebSocketDisconnect
from app.db.sessions import SessionLocal
from app.crud.chat import get_chat_by_id
from app.crud.message import get_message


connected_clients = {}

async def notify_new_message(chat_id: str, message_id: str):
    """Notify connected clients about a new message."""
    db = SessionLocal()
    chat = get_chat_by_id(db, chat_id)  
    message = get_message(db, message_id)  

    if not chat or not message:
        print("Chat or Message not found, skipping notification.")
        return


    for user_id, websocket in connected_clients.items():
        if websocket.application_state == WebSocket.ApplicationState.CONNECTED:
            try:
                await websocket.send_json({
                    "event": "new_message",
                    "chat_id": chat_id,
                    "chat_name": chat.name,
                    "message_id": str(message.id),
                    "message_content": message.content,
                    "sender_id": str(message.sender_id),
                    "timestamp": message.timestamp.isoformat(),
                })
            except Exception as e:
                print(f"Error sending message to user {user_id}: {e}")
                await disconnect_user(user_id)

async def connect_user(user_id: str, websocket: WebSocket):
    """Handle a new WebSocket connection."""
    await websocket.accept()
    connected_clients[user_id] = websocket
    print(f"User {user_id} connected.")

async def disconnect_user(user_id: str):
    """Handle disconnection of a WebSocket client."""
    if user_id in connected_clients:
        del connected_clients[user_id]
        print(f"User {user_id} disconnected.")

async def handle_websocket(websocket: WebSocket, user_id: str):
    """Main WebSocket handler."""
    await connect_user(user_id, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received message from {user_id}: {data}")
    except WebSocketDisconnect:
        await disconnect_user(user_id)
