from fastapi import FastAPI, WebSocket
from app.api.endpoints import user, message, chat, read_receipt, typing_status, attachment, auth
from fastapi.middleware.cors import CORSMiddleware
from app.ws.ws import handle_websocket

app = FastAPI()


origins = [
    "http://localhost:3000",  
    "https://your-production-domain.com",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(message.router, prefix="/messages", tags=["Messages"])
app.include_router(chat.router, prefix="/chats", tags=["Chats"])
app.include_router(read_receipt.router, prefix="/read-receipts", tags=["ReadReceipts"])
app.include_router(typing_status.router, prefix="/typing-status", tags=["TypingStatus"])
app.include_router(attachment.router, prefix="/attachments", tags=["Attachments"])

@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await handle_websocket(websocket, user_id)

@app.get("/")
def root():
    return {"message": "Welcome to Wavve API"}