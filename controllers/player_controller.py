from controllers.base_controller import BaseController
from custom_exception import FormatIDException
from helpers.deserializer import Deserializer
from helpers.helper import Helper
from models.player import Player
from helpers.serializer import Serializer


class PlayerController(BaseController):
    def __init__(self, view):
        super().__init__(view)
        self.accessible_menus = (Helper.get_add_player(),
                                 Helper.get_main_menu())
        self.players_list = None

    def run(self):
        self.players_list = Deserializer.deserialize_players()
        self.view.players_list = self.players_list
        self.view.accessible_menus = self.accessible_menus
        self.view.main_menu_event = self.back_main_menu
        self.view.new_player_event = self.add_new_player
        self.view.run()

        if self.menu_selected == Helper.get_main_menu():
            self.view.new_player_event = None
            self.view.main_menu_event = None
            return Helper.get_main_menu()

    def add_new_player(self, player_data):
        new_player = Player(player_data["player_id"], player_data["name"],
                                         player_data["first_name"], player_data["birth_date"])
        if self.is_player_valid(new_player):
            Serializer.serialize_player(new_player)
            self.players_list.append(new_player)
            # update view
            self.view.update_player_list(new_player)
            self.view.show_new_player_success()
        else:
            self.view.show_new_player_error()

    def back_main_menu(self):
        self.menu_selected  = Helper.get_main_menu()
        self.view.exit()

    def is_player_valid(self, new_player):
        return not any(new_player.player_id == player.player_id for player in self.players_list)