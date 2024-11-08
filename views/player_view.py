from views.basic_view import BasicView


class PlayerView(BasicView):
    def __init__(self):
        super().__init__()
        self.name = "Joueurs"
        self.players_list = []

    def show_menu(self):
        super(PlayerView, self).show_menu()
        print("Joueurs enregistrés : ")
        for player in self.players_list:
            print(player)
        print("1. Ajouter un nouveau joueur")
        print("2. Revenir au menu principal")
        return self.ask_for_user_choice(2)

    def ask_new_player(self):
        print()
        # (bob, marlik, 10/18/2015) ()
