from views.abstract_view import AbstractView
from views.base import IncorrectValueException

class MenuView(AbstractView):

    def __init__(self):
        super().__init__()
        self.name = "Menu principal"

    def show_menu(self):
        """Main menu of the application"""
        super(MenuView, self).show_menu()
        print("1. Créer un tournoi")
        print("2. Lancer un tournoi")
        print("3. Inscrire des joueurs")
        print("4. Générer rapports")
        choice = 0
        while True:
            try:
                choice = int(input("Tapez le numéro correspondant à l'action souhaitée : "))
                if not (1 <= choice <= 4):
                    raise IncorrectValueException("Le nombre doit être compris entre 1 et 4")
            except ValueError:
                print("Veuillez entrer un nombre entier")
            except IncorrectValueException as incorrect_value:
                print(incorrect_value)
            else:
                return choice
