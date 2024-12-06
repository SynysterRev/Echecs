class EmptyStringException(Exception):
    """User enter empty string"""

    def __init__(self):
        message = "Ce champ ne peut être vide"
        super().__init__(message)


class IDException(Exception):
    """User enter incorrect value"""

    def __init__(self, message):
        message = message
        super().__init__(message)


class MenuException(Exception):
    """Menu not created"""

    def __init__(self, message=""):
        message = message
        super().__init__(message)


class ViewException(Exception):
    """View doesn't exist"""

    def __init__(self, view_name):
        message = f"La vue {view_name} n'existe pas"
        super().__init__(message)
