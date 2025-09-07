class BaseSchemaException(Exception):
    pass


class BadPasswordSchemaException(BaseSchemaException):
    def __init__(self):
        super().__init__(
            "Password should contain at least one uppercase letter,"
            " one lowercase letter"
            ", one digit, and one special character @$!%*?&."
        )
