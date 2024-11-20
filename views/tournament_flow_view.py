from custom_exception import OutOfRangeValueException
from helpers.helper import Helper
from views.basic_view import BasicView


class TournamentFlowView(BasicView):
    def __init__(self, console):
        """Menu where user can play a tournament"""
        super().__init__(console)
        self.view_name = "Tournoi"
        self.tournaments = {}
        self.current_round = None
        self.matches = {}
        self.current_match = None

    def tournament_selection(self):
        print("\nTournois enregistrés :")
        print("--------------------------")
        for i in range(len(self.tournaments)):
            print(f"{i + 1}. Tournoi : {self.tournaments[i].view_name}")
        print(f"{len(self.tournaments) + 1}. {Helper.text_menu[Helper.get_main_menu()]}")
        return self.ask_for_user_choice(2, "Tapez le numéro correspondant au tournoi :")

    # def tournament_selection(self):
    #     self.display_all_tournaments()
    #     return self.ask_for_user_choice(2, "Tapez le numéro correspondant au tournoi :")

    def ask_start_round(self):
        print("\nRound :")
        print("--------------------------")
        print(f"1. Démarrer le round {self.current_round}")
        print("2. Retour à la sélection")
        return self.ask_for_user_choice(2)

    def ask_continue_round(self):
        print("\nRound :")
        print("--------------------------")
        print(f"1. Continuer le round {self.current_round}")
        print("2. Retour à la sélection")
        return self.ask_for_user_choice(2)

    def matches_selection(self):
        print("\nMatchs :")
        print("--------------------------")
        for i in range(len(self.matches)):
            print(f"{i + 1}. {self.matches[i]}")
        print(f"{len(self.matches)}. Retour")
        return self.ask_for_user_choice(len(self.matches) + 1, "Tapez le numéro correspondant au match :")

    def ask_match_result(self):
        print("\nRésultat :")
        print("--------------------------")
        print(f"1. {self.current_match.players_score[0][0]}")
        print(f"2. {self.current_match.players_score[1][0]}")
        print(f"3. Match nul")
        return self.ask_for_user_choice(3, "Tapez le numéro correspondant au résultat du match :")

