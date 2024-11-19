import datetime
import re

from colorama import Fore, Style
from custom_exception import OutOfRangeValueException
from helpers.helper import Helper


class BasicView:
    def __init__(self, console):
        self.name = ""
        self.accessible_menus = ()
        self.console = console

    def show_main_menu(self):
        self.show_heading_menu()
        self.display_accessible_menus()
        return self.ask_for_user_choice(len(self.accessible_menus))

    def show_heading_menu(self):
        """Allow some basic formatting for derived views"""
        print("\n" + self.name)
        print("--------------------------")

    def ask_for_user_choice(self, number_max_to_enter, text_to_display="Tapez le numéro correspondant à l'action souhaitée : "):
        choice = int(input(text_to_display))
        if not (1 <= choice <= number_max_to_enter):
            raise OutOfRangeValueException(number_max_to_enter)
        # Since tuples start at 0
        return choice - 1

    def show_type_int_error(self):
        print(Fore.YELLOW)
        print("Veuillez entrer un nombre entier")
        print(Style.RESET_ALL)

    def show_custom_error(self, error):
        print(Fore.YELLOW)
        print(error)
        print(Style.RESET_ALL)

    def show_type_string_error(self):
        print(Fore.YELLOW)
        print("Veuillez entrer une chaîne de caractère")
        print(Style.RESET_ALL)

    def display_accessible_menus(self):
        for i in range(len(self.accessible_menus)):
            # ex : "1. Créer un tournoi"
            print(f"{i + 1}. {Helper.text_menu[self.accessible_menus[i]]}")

    def ask_for_date(self, message_to_display):
        date = str(input(message_to_display))
        return datetime.datetime.strptime(date, "%d/%m/%Y")

    def ask_for_string(self, message_to_display):
        user_input = str(input(message_to_display))
        if not re.search(r"[a-zA-Z]", user_input):
            raise ValueError()
        return user_input

    def ask_for_int(self, message_to_display):
        return str(int(message_to_display))

