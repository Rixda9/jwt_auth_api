# JWT Auth API 

A simple API for JWT token authentication.

## Usage

Start the server:
```bash
uvicorn main:app --reload
```

Register a user:
```bash
curl -X POST http://127.0.0.1:8000/register \
  -H "Content-Type: application/json" \
  -d '{"username":"john", "password":"john123"}'
```

Login and get a token:

```bash
curl -X POST http://127.0.0.1:8000/login \
  -H "Content-Type: application/json" \
  -d '{"username":"john", "password":"john123"}'
```

Access a protected route:
```bash

curl -X GET http://127.0.0.1:8000/protected \
  -H "authorization: your_token_here"
```

## How It Works

User create the account -> It get stored in the database -> They login -> Username and password match -> They get a token -> They can access a protected route with it

## What I Learned

- Hashing
- JWT
- FastAPI
- API Design
- Database Basics
- Salting 
- Pydantic BaseModel 


