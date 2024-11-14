from fastapi import FastAPI, Lifespan
from fastapi.middleware.cors import CORSMiddleware
from app.db.sessions import SessionLocal
from app.db.init_db import init_db
from app.api.endpoints import auth, users, messages, chats

app = FastAPI(lifespan=Lifespan())


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


@app.lifespan
async def lifespan(app: FastAPI):
    with SessionLocal() as db:  
        init_db(db) 

    yield  

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(messages.router, prefix="/messages", tags=["messages"])
app.include_router(chats.router, prefix="/chats", tags=["chats"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Wavve API"} 