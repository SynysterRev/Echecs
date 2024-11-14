import datetime

from views.basic_view import BasicView


class TournamentView(BasicView):
    def __init__(self):
        super().__init__()
        self.name = "Nouveau tournoi"


    def show_menu(self):
        return super().show_menu()

    def ask_tournament_number_rounds(self):
        return int(input("Nombre de rounds (4 par défaut) : ") or 4)

    def ask_tournament_description(self):
        return str(input("Description : "))