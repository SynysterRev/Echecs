import re

from pynput import keyboard

from controllers.base_controller import BaseController
from helpers.deserializer import Deserializer
from helpers.helper import Helper
from helpers.serializer import Serializer
from models.player import Player


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
            with keyboard.Listener(on_press=self.handle_input, suppress=True) as listener:
                listener.join()

            if self.accessible_menus[self.current_selection] == Helper.get_main_menu():
                return Helper.get_main_menu()

            index_field = 0
            self.view.clear_view()
            self.view.render_new_player("")
            method_per_index = {0: self.is_player_id_valid,
                                1: self.is_input_not_empty,
                                2: self.is_input_not_empty,
                                3: self.validate_date}
            new_player_informations = []
            while True:
                final_input = self.get_user_input(self.handle_information_player_input,
                                                  method_per_index[index_field])
                new_player_informations.append(final_input)
                index_field += 1
                if index_field == 4:
                    break
                self.view.change_information_input_index(index_field)
                self.view.validate_information(final_input, index_field - 1)
                self.handle_information_player_input("")
            new_player = Player(new_player_informations[0],
                                               new_player_informations[1],
                                               new_player_informations[2],
                                               new_player_informations[3])
            Serializer.serialize_player(new_player)
            self.players_list.append(new_player)

    def handle_information_player_input(self, user_input):
        self.view.clear_view()
        self.view.render_new_player(user_input)

    def is_player_id_valid(self, new_player_id):
        if re.match(r"^[A-Z]{2}[1-9]{5}$", new_player_id):
            return not any(new_player_id == player.player_id for player in self.players_list)
        return False
