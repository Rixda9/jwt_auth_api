from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel, Field
from database import create_user, get_user, create_db
from auth import hash_comp, create_token, verify_token

create_db()

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

@app.post("/login")
def login(data: Registration):
    user_infos = get_user(data.username)
    if not user_infos:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    if not hash_comp(user_infos[0][2], data.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    else:
        n_token = create_token(data.username)
        return n_token

@app.get("/protected")
def protected(authorization: str = Header(None)):
   
    user = verify_token(authorization)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    else:
        return {"message": f"hello {user['username']}"}


