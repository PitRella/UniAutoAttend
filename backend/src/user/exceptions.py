from fastapi import HTTPException


class BaseUserException(HTTPException):
    """Base class for all custom user exceptions."""



class UserNotFoundException(BaseUserException):
    def __init__(self) -> None:
        super().__init__(
            status_code=404,
            detail='User was not found',
        )
