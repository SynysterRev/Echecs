import datetime
import re

from pynput import keyboard
from blessed import Terminal

from custom_exception import OutOfRangeValueException, CustomException


class BaseController:
    def __init__(self, view):
        """Base controller

        accessible_menus: id of all the menus that we can access from here
        view: view managed by the controller
        """
        self.view = view
        self.accessible_menus = ()
        self.current_selection = 0

    def run(self):
        self.view.accessible_menus = self.accessible_menus
        self.view.clear_view()
        self.view.render(self.current_selection)
        with keyboard.Listener(on_press=self.handle_input, suppress=True) as listener:
            listener.join()
        return self.accessible_menus[self.current_selection]

    def get_user_choice(self, method_to_call) -> int:
        while True:
            try:
                choice = method_to_call()
            except ValueError:
                self.view.show_type_int_error()
            except OutOfRangeValueException as exception:
                self.view.show_custom_error(exception)
            else:
                return choice

    def get_date_from_user(self, view_method, message_to_display):
        while True:
            try:
                date = view_method(message_to_display)
            except ValueError:
                self.view.show_custom_error("La date n'est pas au format jj/mm/aaaa")
            else:
                break
        return date.strftime("%d/%m/%Y")

    def get_string_from_user(self, message_to_display):
        while True:
            try:
                user_string = self.view.ask_for_string(message_to_display)
            except ValueError:
                self.view.show_type_string_error()
            else:
                return user_string

    def get_int_from_user(self, message_to_display):
        while True:
            try:
                user_int = self.view.ask_for_int(message_to_display)
            except ValueError:
                self.view.show_type_int_error()
            else:
                return user_int

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
        self.current_selection = (self.current_selection - 1) % len(self.accessible_menus)
        self.view.clear_view()
        self.view.render(self.current_selection)

    def move_down(self):
        self.current_selection = (self.current_selection + 1) % len(self.accessible_menus)
        self.view.clear_view()
        self.view.render(self.current_selection)

    def is_input_not_empty(self, user_input):
        for char in user_input:
            if char != " ":
                return True

    def is_input_int(self, user_input):
        try:
            int(user_input)
            return True
        except ValueError:
            return False

    def validate_date(self, date):
        try:
            datetime.datetime.strptime(date, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    def get_user_input(self, view_func, validate_func):
        term = Terminal()
        user_input = ""
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
                    view_func(user_input)
