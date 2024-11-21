import threading

from typing_extensions import overload

from custom_exception import OutOfRangeValueException

class BaseController:
    def __init__(self, view):
        """Base controller

        accessible_menus: id of all the menus that we can access from here
        view: view managed by the controller
        """
        self.view = view
        self.accessible_menus = ()
        self.menu_selected = None

    def run(self):
        self.view.accessible_menus = self.accessible_menus
        self.view.subscribe(self.on_click)
        self.view.run()

        return self.menu_selected

    def on_click(self, value):
        self.menu_selected = value
        self.view.unsubscribe(self.on_click)
        self.view.exit()

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