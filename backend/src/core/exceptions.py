from fastapi import HTTPException

class BaseHttpException(HTTPException):
    """Base class for all custom HTTP exceptions."""

class ForgottenParametersException(BaseHttpException):
    """Exception raised when required parameters are missing."""

    def __init__(self) -> None:
        """Initialize ForgottenParametersException with status 422."""
        super().__init__(
            status_code=422,
            detail='Fill at least one parameter',
        )