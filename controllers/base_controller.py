import sys
from time import sleep

import keyboard

from custom_exception import OutOfRangeValueException, CustomException
from rich.live import Live


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
        running = True
        while running:
            running = self.handle_input()
        # with Live(self.view.render(self.current_selection), refresh_per_second=10) as live:

                # live.update(self.view.render(self.current_selection))
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

    def handle_input(self):
        """Handle user input
            return False if the user select a menu"""
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and keyboard.is_pressed("up"):
            self.move_up()
        if event.event_type == keyboard.KEY_DOWN and keyboard.is_pressed("down"):
            self.move_down()
        if event.event_type == keyboard.KEY_DOWN and keyboard.is_pressed("enter"):
            return False
        return True

    def move_up(self):
        self.current_selection = (self.current_selection - 1) % len(self.accessible_menus)
        self.view.clear_view()
        self.view.render(self.current_selection)

    def move_down(self):
        self.current_selection = (self.current_selection + 1) % len(self.accessible_menus)
        self.view.clear_view()
        self.view.render(self.current_selection)

    def ask_prompt_with_validation(self, view_method, validate_func=None,
                                   error_message="Veuillez réessayer"):
        while True:
            user_input = view_method()
            if validate_func is not None:
                try:
                    if validate_func(user_input):
                        return user_input
                    else:
                        raise CustomException
                except CustomException:
                    self.view.show_custom_error(error_message)
