from controllers.base_controller import BaseController
from helpers.deserializer import Deserializer
from helpers.helper import Helper
from helpers.serializer import Serializer


class PlayerController(BaseController):
    def __init__(self, view):
        super().__init__(view)
        self.accessible_menus = (Helper.get_add_player(),
                                 Helper.get_main_menu())
        self.players_list = []

    def run(self):
        self.players_list = Deserializer.deserialize_players()
        self.view.players_list = self.players_list
        self.view.accessible_menus = self.accessible_menus
        self.max_selection = len(self.accessible_menus)
        while True:
            self.view.clear_view()
            self.view.render(self.current_selection)
            self.handle_input()

            if self.accessible_menus[self.current_selection] == Helper.get_main_menu():
                return Helper.get_main_menu()

            new_player = self.ask_for_new_player()
            Serializer.serialize_player(new_player)
            self.players_list.append(new_player)
            self.view.clear_player_informations()

    def handle_information_player_input(self):
        self.view.clear_view()
        self.view.render_new_player()
