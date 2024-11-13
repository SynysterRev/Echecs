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
                while True:
                    try:
                        birth_date = self.view.ask_player_birth_date()
                    except ValueError:
                        self.view.show_custom_error("La date de naissance n'est pas au format jj/mm/aaaa")
                    else:
                        break
                string_date = birth_date.strftime("%d/%m/%Y")
                Serializer.serialize_player(Player(name, first_name, string_date))
                # update view
                self.view.players_list = Deserializer.deserialize_players()
            else:
                return Helper.get_main_menu()
