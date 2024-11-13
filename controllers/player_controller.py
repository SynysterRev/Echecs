from controllers.base_controller import BaseController
from helpers.deserializer import Deserializer
from helpers.helper import Helper
from models.player import Player
from helpers.serializer import Serializer


class PlayerController(BaseController):
    def __init__(self, view):
        super().__init__(view)
        self.accessible_menus = (Helper.get_add_player(),
                                 Helper.get_quit())

    def run(self):
        players_list = Deserializer.deserialize_players()
        self.view.players_list = players_list
        self.view.accessible_menus = self.accessible_menus
        while True:
            choice = self.get_user_choice()
            if choice == 0:
                name = self.view.ask_player_name()
                first_name = self.view.ask_player_first_name()
                birth_date = self.get_date_from_user(self.view.ask_for_date,
                                                     "Date de naissance (ex : 01/01/1900) : ")
                Serializer.serialize_player(Player(name, first_name, birth_date))
                # update view
                self.view.players_list = Deserializer.deserialize_players()
            else:
                return Helper.get_main_menu()
