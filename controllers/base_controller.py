import datetime

from blessed import Terminal
from pynput import keyboard

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
        with keyboard.Listener(on_press=self.handle_input, suppress=True) as listener:
            listener.join()
        return self.accessible_menus[self.current_selection]

    def handle_input(self, key):
        """Handle user input
           return False if the user select a menu -> we don't need to wait for the user input anymore"""
        if key == keyboard.Key.up:
            self.move_up()
        if key == keyboard.Key.down:
            self.move_down()
        if key == keyboard.Key.enter:
            return False

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
            int(user_input)
            return True
        except ValueError:
            raise EmptyStringException()

    def validate_date(self, date):
        try:
            is_date = bool(datetime.datetime.strptime(date, "%d/%m/%Y"))
            return is_date
        except ValueError:
            raise ValueError("La date doit être au format JJ/MM/AAAA")

    # handle arrow character
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
                    else:
                        user_input += key
                    self.view.current_input = user_input
                    view_func()
