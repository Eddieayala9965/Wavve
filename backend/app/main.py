from fastapi import FastAPI
from app.api.endpoints import user, message, chat, read_receipt, typing_status, attachment
from fastapi.middleware.cors import CORSMiddleware

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

app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(message.router, prefix="/messages", tags=["Messages"])
app.include_router(chat.router, prefix="/chats", tags=["Chats"])
app.include_router(read_receipt.router, prefix="/read-receipts", tags=["ReadReceipts"])
app.include_router(typing_status.router, prefix="/typing-status", tags=["TypingStatus"])
app.include_router(attachment.router, prefix="/attachments", tags=["Attachments"])

@app.get("/")
def root():
    return {"message": "Welcome to Wavve API"}