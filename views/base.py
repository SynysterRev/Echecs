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

class View:
    def __init__(self, active_view, views):
        self.active_view = active_view
        self.views = views

    def show_menu(self):
        self.active_view.show_menu()