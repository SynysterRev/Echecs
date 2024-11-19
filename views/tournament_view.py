import datetime

from custom_exception import OutOfRangeValueException
from views.basic_view import BasicView


class TournamentView(BasicView):
    """Menu where user can manage tournaments"""
    def __init__(self, console):
        super().__init__(console)
        self.name = "Gestion de tournoi"
        self.tournaments = {}

    def ask_tournament_number_rounds(self):
        return int(input("Nombre de rounds (4 par défaut) : ") or 4)

    def ask_tournament_description(self):
        return str(input("Description : "))

    def tournament_created(self):
        print("Le tournoi a été créé avec succès")

    def display_all_tournaments(self):
        print("\nTournois enregistrés :")
        print("--------------------------")
        for i in range(len(self.tournaments)):
            print(f"{i + 1}. Tournoi : {self.tournaments[i].name}")
        print(f"{len(self.tournaments) + 1}. Retour")

    def ask_tournament_selection(self):
        choice = int(input("Tapez le numéro correspondant au tournoi : "))
        # +1 cause we want to go back to previous menu
        number_max_to_enter = len(self.tournaments) + 1
        if not (1 <= choice <= number_max_to_enter):
            raise OutOfRangeValueException(number_max_to_enter)
        # Since tuples start at 0
        return choice - 1

    def tournament_selection(self):
        self.display_all_tournaments()
        return self.ask_tournament_selection()
