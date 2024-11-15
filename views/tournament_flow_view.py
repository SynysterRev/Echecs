from custom_exception import OutOfRangeValueException
from helpers.helper import Helper
from views.basic_view import BasicView


class TournamentFlowView(BasicView):
    def __init__(self):
        """Menu where user can play a tournament"""
        super().__init__()
        self.name = "Tournoi"
        self.tournaments = {}

    def display_all_tournaments(self):
        print("\nTournois enregistrés :")
        print("--------------------------")
        for i in range(len(self.tournaments)):
            print(f"{i + 1}. Tournoi : {self.tournaments[i].name}")
        print(f"{len(self.tournaments) + 1}. {Helper.text_menu[Helper.get_main_menu()]}")

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

    def ask_start_round(self, current_round):
        print(f"1. Démarrer le tour {current_round}")
        print("2. Retour à la sélection")
        return self.ask_for_user_choice(2)
