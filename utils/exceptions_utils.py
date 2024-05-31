from fastapi import status
from fastapi.exceptions import HTTPException


class NotAuthorizedException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not authorized")
