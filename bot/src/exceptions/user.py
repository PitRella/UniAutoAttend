

class NoUserException(Exception):
    def __init__(self):
        super().__init__("Cannot get user from message")

class NoCallbackDataException(Exception):
    def __init__(self):
        super().__init__("Cannot get callback data from message")
class NoPreviousMessageException(Exception):
    def __init__(self):
        super().__init__("Cannot get previous message from message")

class InvalidLanguageException(Exception):
    def __init__(self):
        super().__init__("Invalid language")

class NoUserDataExceptions(Exception):
    def __init__(self):
        super().__init__(
            "User data is not set. Please use /start command to set user data"
        )