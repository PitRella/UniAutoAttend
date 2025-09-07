

class NoUserException(Exception):
    def __init__(self):
        super().__init__("Cannot get user from message")