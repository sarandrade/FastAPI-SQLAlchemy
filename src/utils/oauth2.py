from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from .token import decode_token

OAUTH2_SCHEMA = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(OAUTH2_SCHEMA)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid Credentials!",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return decode_token(token, credentials_exception)
