from dotenv import load_dotenv
import os
import bcrypt
import jwt


load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')


def hash_func(password):

# password to array of bytes
    encoded = password.encode('utf-8')

# salt
    salt = bcrypt.gensalt()

# hash 
    hashed = bcrypt.hashpw(encoded, salt)

    return hashed


def hash_comp(hashed, password):

    encoded = password.encode('utf-8')

    isSame = bcrypt.checkpw(encoded, hashed)

    return isSame

def create_token(username):
    
    payload = {"username": username}

    jwt_tok = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return jwt_tok

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.InvalidTokenError:
        return None
    
