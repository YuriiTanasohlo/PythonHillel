class GroupException(Exception):
    def __init__(self, message):
        super().__init__(message)


class OverloadedGroupException(GroupException):
    def __init__(self, message):
        super().__init__(message)
