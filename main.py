from fastapi import FastAPI 
from pydantic import BaseModel, Field
from database import create_user

class Registration(BaseModel):
    username: str 
    password: str = Field(..., min_length=8)

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/register")
def register(data: Registration):
    create_user(data.username, data.password) 
    return {"message": "User created successfully"}

