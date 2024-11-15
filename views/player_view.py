import datetime

from views.basic_view import BasicView


class PlayerView(BasicView):
    """Menu where user can add new players to the database"""
    def __init__(self):
        super().__init__()
        self.name = "Joueurs enregistrés"
        self.players_list = []

    def show_main_menu(self):
        self.show_heading_menu()
        for player in self.players_list:
            print(player)
        print()
        self.display_accessible_menus()
        return self.ask_for_user_choice(2)

    def ask_player_name(self):
        return str(input("Nom : "))

    def ask_player_first_name(self):
        return str(input("Prenom : "))
