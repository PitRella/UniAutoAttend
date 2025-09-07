

class NoUserException(Exception):
    def __init__(self):
        super().__init__("Cannot get user from message")

class NoCallbackDataException(Exception):
    def __init__(self):
        super().__init__("Cannot get callback data from message")