from colorama import Fore, Style

from views.base import OutOfRangeValueException

class BasicView:
    def __init__(self):
        self.name = ""

    def show_menu(self):
        """Allow some basic formatting for derived views"""
        print(self.name)
        print("--------------------------")

    def ask_for_user_choice(self, number_max_to_enter):
            choice = int(input("Tapez le numéro correspondant à l'action souhaitée : "))
            if not (1 <= choice <= number_max_to_enter):
                 raise OutOfRangeValueException(number_max_to_enter)
            # Since tuples start at 0
            return choice - 1

    def show_type_value_error(self):
        print(Fore.YELLOW)
        print("Veuillez entrer un nombre entier")
        print(Style.RESET_ALL)

    def show_custom_error(self, error):
        print(Fore.YELLOW)
        print(error)
        print(Style.RESET_ALL)