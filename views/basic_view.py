import datetime
import re
import os

from colorama import Fore, Style
from custom_exception import OutOfRangeValueException
from helpers.helper import Helper
from rich.text import Text
from rich.table import Table
from rich.align import Align
from rich.panel import Panel
from rich.prompt import Prompt


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

    def ask_for_user_choice(self, number_max_to_enter,
                            text_to_display="Tapez le numéro correspondant à l'action souhaitée : "):
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
        self.console.print(f"[red]{error}[/red]")

    def show_type_string_error(self):
        print(Fore.YELLOW)
        print("Veuillez entrer une chaîne de caractère")
        print(Style.RESET_ALL)

    def display_accessible_menus(self):
        for i in range(len(self.accessible_menus)):
            # ex : "1. Créer un tournoi"
            print(f"{i + 1}. {Helper.text_menu[self.accessible_menus[i]]}")

    def ask_for_date(self, message_to_display):
        date = str(Prompt.ask(message_to_display))
        return datetime.datetime.strptime(date, "%d/%m/%Y")

    def ask_for_string(self, message_to_display):
        user_input = str(input(message_to_display))
        if not re.search(r"[a-zA-Z]", user_input):
            raise ValueError()
        return user_input

    def ask_for_int(self, message_to_display):
        return str(int(message_to_display))

    def render(self, current_selection):
        table = self.get_table_menu(current_selection)

        panel_title = f"[bold magenta]{self.name}[/bold magenta]"

        self.console.print(Panel(Align.center(table), title=panel_title))

    def clear_view(self):
        # self.console.clear()
        self.cls()

    def get_table_menu(self, current_selection):
        table = Table.grid(padding=1)
        table.add_column(justify="center")
        for index, menu in enumerate(self.accessible_menus):
            if index == current_selection:
                option_style = "bold white on blue"
            else:
                option_style = "white"

            option_text = Text(Helper.text_menu[menu], style=option_style)
            table.add_row(option_text)
        return table

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')