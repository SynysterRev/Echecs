class NoTournamentException(Exception):
    '''No tournament selected'''

    def __init__(self, message=""):
        message = message or "No tournament selected"
        super().__init__(message)


class OutOfRangeValueException(Exception):
    """User enter incorrect value"""

    def __init__(self, max_value):
        message = f"Le nombre doit être compris entre 1 et " + str(max_value)
        super().__init__(message)


class FormatIDException(Exception):
    """User enter incorrect value"""

    def __init__(self):
        message = "L'identifiant doit comporter 2 lettres suivies de 5 chiffres (AB12345)"
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
