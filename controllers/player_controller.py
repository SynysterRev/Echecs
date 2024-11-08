from deserializer import Deserializer
from views.player_view import PlayerView


class PlayerController:
    def __init__(self):
        self.view = PlayerView()


    def run(self):
        players_list = Deserializer.deserialize_players()
        self.view.players_list = players_list
        choice = self.view.show_menu()
        if choice == 1:
            print()
        else:
            return "main_menu"