from helper import Helper
from views.basic_view import BasicView
from views.base import IncorrectValueException

class MenuView(BasicView):

    def __init__(self):
        super().__init__()
        self.name = "Menu principal"
        self.accessible_menus = ()

    def show_menu(self):
        """Main menu of the application"""
        super(MenuView, self).show_menu()

        for i in range(len(self.accessible_menus)):
            # ex : "1. Créer un tournoi"
            print(f"{i + 1}. {Helper.text_menu[self.accessible_menus[i]]}")
        while True:
            try:
                choice = int(input("Tapez le numéro correspondant à l'action souhaitée : "))
                if not (1 <= choice <= len(self.accessible_menus)):
                    raise IncorrectValueException(f"Le nombre doit être compris entre 1 et {len(self.accessible_menus)}")
            except ValueError:
                print("Veuillez entrer un nombre entier")
            except IncorrectValueException as incorrect_value:
                print(incorrect_value)
            else:
                # Since tuples start at 0
                return choice - 1
