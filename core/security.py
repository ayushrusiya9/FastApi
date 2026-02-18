from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.core.config import settings
from fastapi import HTTPException
from passlib.context import CryptContext

# create password context
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(password:str, hashed_password:str):
    return pwd_context.verify(password, hashed_password)


# create jwt token 
def create_token(data : str):
    to_encode = {}
    minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    expire = datetime.utcnow() + timedelta(minutes=minutes)
    data.update({"exp":expire})
    to_encode.update({"exp":datetime})
    encode_jwt = jwt.encode(data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encode_jwt

# decode token or verify access token jwt
def decode_token(token:str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    