from datetime import datetime

from blessed import Terminal

from custom_exception import EmptyStringException


class BaseController:
    def __init__(self, view):
        """Base controller

        accessible_menus: id of all the menus that we can access from here
        view: view managed by the controller
        """
        self.view = view
        self.accessible_menus = ()
        self.current_selection = 0
        self.max_selection = 0

    def run(self):
        self.view.accessible_menus = self.accessible_menus
        self.view.clear_view()
        self.view.render(self.current_selection)
        self.max_selection = len(self.accessible_menus)
        self.handle_input()
        return self.accessible_menus[self.current_selection]

    def handle_input(self):
        """Handle user input
           return False if the user select a menu -> we don't need to wait for the user input anymore"""

        term = Terminal()
        with term.cbreak():
            while True:
                key = term.inkey(timeout=0.1)
                if key:
                    if key.name == "KEY_ENTER":
                        return False
                    elif key.name == "KEY_UP":
                        self.move_up()
                    elif key.name == "KEY_DOWN":
                        self.move_down()

    def move_up(self):
        self.current_selection = (self.current_selection - 1) % self.max_selection
        self.render_view()

    def move_down(self):
        self.current_selection = (self.current_selection + 1) % self.max_selection
        self.render_view()

    def render_view(self):
        self.view.clear_view()
        self.view.render(self.current_selection)

    def is_input_not_empty(self, user_input):
        if len(user_input) > 0 and user_input[0] != " ":
            return True
        else:
            raise EmptyStringException()

    def is_input_int(self, user_input):
        try:
            int_input = int(user_input)
            if int_input > 0:
                return True
            else:
                raise ValueError()
        except ValueError:
            raise ValueError("Veuillez entrer un nombre positif et supérieur à 0")

    def validate_date(self, date):
        try:
            is_date = bool(datetime.strptime(date, "%d/%m/%Y"))
            return is_date
        except ValueError:
            raise ValueError("La date doit être au format JJ/MM/AAAA")

    def get_user_input(self, view_func, validate_func, default_input=""):
        term = Terminal()
        user_input = default_input
        with term.cbreak():
            while True:
                key = term.inkey(timeout=0.1)
                if key:
                    if key.name == "KEY_ENTER":
                        if validate_func(user_input):
                            return user_input
                    elif key.name == "KEY_BACKSPACE":
                        user_input = user_input[:-1]
                        self.view.current_input = user_input
                        view_func()
                    # avoid special key like arrow or F1 to be counted
                    elif key.name is None:
                        user_input += key
                        self.view.current_input = user_input
                        view_func()
