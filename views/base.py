class IncorrectValueException(Exception):
    """User enter incorrect value"""

    def __init__(self, message=""):
        message = message
        super().__init__(message)

class View:
    def __init__(self, active_view, views):
        self.active_view = active_view
        self.views = views

    def show_menu(self):
        self.active_view.show_menu()